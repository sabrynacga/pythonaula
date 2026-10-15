# ============================================
#    PRÁTICA INDEPENDENTE - 6 MINI-DESAFIOS
# ============================================

# -----------------------------------------------
# PARTE 1
# -----------------------------------------------

# Desafio 1: Calculadora de troco
print("=== Desafio 1: Calculadora de Troco ===")
valor_compra = float(input("Digite o valor da compra: R$ "))
valor_pago = float(input("Digite o valor pago: R$ "))
troco = valor_pago - valor_compra
print(f"Troco a devolver: R$ {troco:.2f}\n")

# -----------------------------------------------

# Desafio 2: Conversor de tempo
print("=== Desafio 2: Conversor de Tempo ===")
segundos_total = int(input("Digite a quantidade de segundos: "))
horas = segundos_total // 3600
minutos = (segundos_total % 3600) // 60
segundos = segundos_total % 60
print(f"{segundos_total} segundos = {horas}h {minutos}min {segundos}s\n")

# -----------------------------------------------

# Desafio 3: Par ou ímpar
print("=== Desafio 3: Par ou Ímpar ===")
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"{numero} é PAR\n")
else:
    print(f"{numero} é ÍMPAR\n")

# -----------------------------------------------
# PARTE 2
# -----------------------------------------------

# Desafio 4: Média de notas
print("=== Desafio 4: Média de Notas ===")
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"Média das notas: {media:.2f}\n")

# -----------------------------------------------

# Desafio 5: Calculadora de desconto
print("=== Desafio 5: Calculadora de Desconto ===")
preco = float(input("Digite o preço do produto: R$ "))
percentual = float(input("Digite o percentual de desconto (%): "))
desconto = preco * (percentual / 100)
preco_final = preco - desconto
print(f"Desconto de {percentual}%: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}\n")

# -----------------------------------------------

# Desafio 6: Inversor de nome
print("=== Desafio 6: Inversor de Nome ===")
nome = input("Digite um nome: ")
nome_invertido = nome[::-1]
print(f"Nome invertido: {nome_invertido}\n")

