print("1-Soma | 2-Subtração | 3-Multiplicação | 4-Divisão")
op = int(input("Escolha: "))
n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))

match op:
    case 1: print(f"Resultado: {n1 + n2}")
    case 2: print(f"Resultado: {n1 - n2}")
    case 3: print(f"Resultado: {n1 * n2}")
    case 4: print(f"Resultado: {n1 / n2}" if n2 != 0 else "Erro: Divisão por zero")
    case _: print("Operação inválida")