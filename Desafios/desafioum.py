#Pilha de três torres
#nunca coloque um disco maior sobre um menor
#mover apenas um disco por vez
#a cada movimento, imprimir as três torres no formato de listas

def mover_disco(n, origem, destino, auxiliar):
    if n == 1:
        disco = origem.pop()
        destino.append(disco)
        print(f"Movendo disco {disco} de {origem} para {destino}")
    else:
        mover_disco(n - 1, origem, auxiliar, destino)
        mover_disco(1, origem, destino, auxiliar)
        mover_disco(n - 1, auxiliar, destino, origem)
