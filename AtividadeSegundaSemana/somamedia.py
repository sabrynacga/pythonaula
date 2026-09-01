soma = 0
maior = float('-inf')
menor = float('inf')

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    soma += num
    if num > maior: maior = num
    if num < menor: menor = num

media = soma / 5
print(f"Soma: {soma}\nMédia: {media}\nMaior: {maior}\nMenor: {menor}")