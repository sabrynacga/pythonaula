idade = int(input("Digite a idade: "))
renda = float(input("Digite a renda: "))

if idade < 18:
    print("Cliente não elegível para classificação.")
elif renda <= 2000:
    print("Categoria: Bronze")
elif renda <= 5000:
    print("Categoria: Prata")
elif renda <= 10000:
    print("Categoria: Ouro")
else:
    print("Categoria: Diamante")