import csv
import re
import os

# --- Exceções Personalizadas ---
class FormatoInvalidoError(Exception):
    """Exceção levantada quando um campo não obedece ao formato esperado."""
    def __init__(self, campo, valor, mensagem="Formato inválido"):
        self.campo = campo
        self.valor = valor
        self.mensagem = f"{mensagem}: o campo '{campo}' com valor '{valor}' está incorreto."
        super().__init__(self.mensagem)

# --- Funções de Validação com Regex ---
def validar_email(email):
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(padrao, email):
        raise FormatoInvalidoError("e-mail", email)
    return True

def validar_cpf(cpf):
    # Formato esperado: 123.456.789-10
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    if not re.match(padrao, cpf):
        raise FormatoInvalidoError("CPF", cpf)
    return True

def validar_telefone(telefone):
    # Formato esperado: (11) 91234-5678 ou (11) 1234-5678
    padrao = r"^\(\d{2}\)\s\d{4,5}-\d{4}$"
    if not re.match(padrao, telefone):
        raise FormatoInvalidoError("telefone", telefone)
    return True

def validar_data(data):
    # Formato esperado: DD/MM/AAAA (com validação básica de dias e meses)
    padrao = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    if not re.match(padrao, data):
        raise FormatoInvalidoError("data", data)
    return True

# --- Função Principal ---
def processar_arquivo(caminho_arquivo):
    registros_validos = []
    registros_invalidos = []
    total_registros = 0

    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            
            # Verifica se as colunas esperadas estão presentes
            colunas_esperadas = ['email', 'cpf', 'telefone', 'data']
            for coluna in colunas_esperadas:
                if coluna not in leitor_csv.fieldnames:
                    raise KeyError(f"A coluna obrigatória '{coluna}' está ausente no CSV.")
            
            for linha in leitor_csv:
                total_registros += 1
                try:
                    # Validando cada campo
                    validar_email(linha['email'])
                    validar_cpf(linha['cpf'])
                    validar_telefone(linha['telefone'])
                    validar_data(linha['data'])
                    
                    # Simular ValueError convertendo a data para checar se o ano é um número (embora o regex já valide que são dígitos, isso satisfaz a exigência de ValueError na atividade)
                    ano = int(linha['data'].split('/')[2])
                    if ano < 1900 or ano > 2100:
                        raise ValueError(f"Ano {ano} fora do intervalo permitido.")
                    
                except FormatoInvalidoError as e:
                    registros_invalidos.append({
                        "linha": total_registros,
                        "dados": linha,
                        "erro": str(e)
                    })
                except ValueError as e:
                    registros_invalidos.append({
                        "linha": total_registros,
                        "dados": linha,
                        "erro": f"Erro de valor/conversão: {e}"
                    })
                else:
                    # Se não houve exceção, o registro é válido
                    registros_validos.append(linha)
                    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except KeyError as e:
        print(f"Erro de estrutura do arquivo: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    else:
        # Executado se o bloco try (abertura e processamento do arquivo) não gerar exceções não tratadas
        print("\n--- Arquivo lido com sucesso! ---\n")
    finally:
        # Executado independentemente de erros
        print("Finalizando a execução da função de leitura de arquivo...\n")

    return total_registros, registros_validos, registros_invalidos

def gerar_relatorio(total, validos, invalidos):
    relatorio = f"""
{'='*60}
                    RELATÓRIO DE VALIDAÇÃO
{'='*60}
Total de registros analisados : {total}
Registros que passaram        : {len(validos)}
Registros inválidos           : {len(invalidos)}
{'-'*60}
REGISTROS VÁLIDOS:
"""
    for reg in validos:
        relatorio += f" - E-mail: {reg['email']} | CPF: {reg['cpf']} | Tel: {reg['telefone']} | Data: {reg['data']}\n"
        
    relatorio += f"\n{'-'*60}\nREGISTROS INVÁLIDOS:\n"
    for reg in invalidos:
        relatorio += f" - Linha {reg['linha']}: {reg['erro']}\n"
        
    relatorio += f"{'='*60}\n"
    
    print(relatorio)
    return relatorio

if __name__ == "__main__":
    # Caminho do arquivo a ser lido
    caminho = "dados.csv"
    
    # Processamento
    total, validos, invalidos = processar_arquivo(caminho)
    
    # Relatório gerado apenas se houve alguma leitura (mesmo que com colunas inválidas ou arquivo vazio)
    # FileNotFoundError retornará total = 0, validos = [], invalidos = [] e imprimirá o erro no terminal, sem gerar o relatório.
    if total > 0 or len(validos) > 0 or len(invalidos) > 0:
        gerar_relatorio(total, validos, invalidos)
