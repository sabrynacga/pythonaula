senha_correta = "12345"
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")
    
    if senha == senha_correta:
        print("Acesso liberado!")
        break
    else:
        tentativas += 1
        print(f"Senha incorreta. Restam {3 - tentativas} tentativa(s).")

if tentativas == 3:
    print("Conta bloqueada por excesso de tentativas.")