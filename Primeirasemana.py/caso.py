print("=== MENU DE INSCRIÇÃO DA MARATONA ===")
print("1 - Maratona completa")
print("2 - Meia maratona")
print("3 - Corrida de Estreia")

opcao = int(input("Escolha o numero da sua categoria: "))
match opcao:
    case 1:
        print("Inscrição confirmada: Maratona Completa (42.195 km)")
    case 2:
        print("Inscrição confirmada: Meia Maratona (21.097 km)")
    case 3:
        print("Inscrição confirmada: Corrida de Estreia (5 km)")
    case _:
        print("Erro: Categoria inexistente! Escolha de 1 a 3.")