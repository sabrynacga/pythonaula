nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"Média: {media:.2f}")
if media >= 7.0:
    print("CLASSIFICAÇÃO: Aprovado")
elif media >= 5.0:
    print("CLASSIFICAÇÃO: Recuperação")
else:
    print("CLASSIFICAÇÃO: Reprovado")
