# Atividade da Quinta Semana - Validação de Dados

Este projeto é um script em Python que lê um arquivo de dados (`dados.csv`), realiza a validação de seus campos através de Expressões Regulares (Regex) e gera um relatório formatado das linhas processadas.

## Justificativa das Validações Aplicadas (Regex)

As validações foram implementadas utilizando o módulo `re` do Python para garantir que os dados de cada linha do arquivo obedeçam aos formatos padrões especificados.

- **E-mail (`r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"`):**
  - Justificativa: Valida se há caracteres alfanuméricos e permitidos antes e depois do `@`, e um domínio válido terminando com no mínimo dois caracteres para o país ou tipo de domínio (ex: `.com`, `.br`). O uso de `^` e `$` garante que toda a string obedeça ao formato, sem trechos residuais.
- **CPF (`r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"`):**
  - Justificativa: Garante exatamente o padrão `XXX.XXX.XXX-XX`, em que `\d` representa dígitos de 0 a 9.
- **Telefone (`r"^\(\d{2}\)\s\d{4,5}-\d{4}$"`):**
  - Justificativa: Garante que o telefone possua o formato `(XX) XXXXX-XXXX` ou `(XX) XXXX-XXXX` (com 4 ou 5 dígitos antes do hífen). O `\s` é utilizado para forçar um espaço após o DDD.
- **Data (`r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"`):**
  - Justificativa: Verifica se a data segue o formato `DD/MM/AAAA`. A validação foi refinada para só aceitar dias de `01` a `31` e meses de `01` a `12`. Além disso, para fins de validação adicional de negócio, um bloco de conversão foi adicionado no código principal para verificar se o ano está dentro de um limite aceitável.

## Explicação das Exceções Tratadas

O código faz o uso de blocos `try/except/else/finally` para tornar o sistema mais resiliente:

1. **`FileNotFoundError`**: Capturada caso o script seja executado e o arquivo `dados.csv` não exista no diretório especificado.
2. **`KeyError`**: Levantada intencionalmente caso o arquivo CSV não possua os cabeçalhos das colunas obrigatórias (`email`, `cpf`, `telefone`, `data`). Isso evita que o programa quebre internamente tentando acessar um índice inexistente de um dicionário.
3. **`ValueError`**: Tratada caso ocorra algum problema de valor ou conversão incorreta. No código, o ano da data validada é convertido em `int()`. Caso ele ultrapasse limites irreais (menor que 1900 ou maior que 2100), levantamos essa exceção para demonstrar uma regra de negócio que vai além do regex puro.
4. **`FormatoInvalidoError`**: Esta é uma classe de Exceção Personalizada criada neste script (que herda de `Exception`). Ela é instanciada e levantada toda vez que uma das funções de validação por regex falha, facilitando a identificação do campo e o valor que geraram o erro.

## Exemplo de Entrada (`dados.csv`)

O script deve ser alimentado por um arquivo `.csv` que contenha a seguinte estrutura:

```csv
email,cpf,telefone,data
joao.silva@email.com,123.456.789-10,(11) 98765-4321,15/08/1990
maria_oliveira@dominio.br,987.654.321-00,(21) 91234-5678,22/11/1985
email.invalido.com,111.222.333-44,(31) 3214-5678,01/01/2000
carlos@teste.com,cpf-invalido-aqui,(41) 99999-9999,10/10/1995
ana@exemplo.com,555.666.777-88,11 988887777,05/05/1992
fernanda@site.com,444.555.666-77,(61) 96666-5555,10/10/3000
```

## Exemplo de Saída (Relatório Gerado)

Após o processamento do arquivo de entrada, caso ele exista, o terminal exibirá as execuções do `else` e `finally` do bloco de leitura e, por fim, o relatório em `f-strings`:

```text
--- Arquivo lido com sucesso! ---

Finalizando a execução da função de leitura de arquivo...

============================================================
                    RELATÓRIO DE VALIDAÇÃO
============================================================
Total de registros analisados : 8
Registros que passaram        : 3
Registros inválidos           : 5
------------------------------------------------------------
REGISTROS VÁLIDOS:
 - E-mail: joao.silva@email.com | CPF: 123.456.789-10 | Tel: (11) 98765-4321 | Data: 15/08/1990
 - E-mail: maria_oliveira@dominio.br | CPF: 987.654.321-00 | Tel: (21) 91234-5678 | Data: 22/11/1985
 - E-mail: pedro@dominio.com | CPF: 222.333.444-55 | Tel: (51) 8888-8888 | Data: 31/12/2023

------------------------------------------------------------
REGISTROS INVÁLIDOS:
 - Linha 3: Formato inválido: o campo 'e-mail' com valor 'email.invalido.com' está incorreto.
 - Linha 4: Formato inválido: o campo 'CPF' com valor 'cpf-invalido-aqui' está incorreto.
 - Linha 5: Formato inválido: o campo 'telefone' com valor '11 988887777' está incorreto.
 - Linha 7: Formato inválido: o campo 'data' com valor '40/12/2020' está incorreto.
 - Linha 8: Erro de valor/conversão: Ano 3000 fora do intervalo permitido.
============================================================
```
