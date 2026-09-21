def caixa(*precos):
    if not precos:
        return 0, 0, 0
    total = sum(precos)
    mais_caro = max(precos)
    media = total / len(precos)
    return total, mais_caro, media