# Solução do sistema de gestão de produtos[cite: 1]

produtos = []
precos = []

print("--- Registo de Produtos ---")
# Cadastro de Produtos utilizando input() e append()[cite: 1]
while True:
    nome = input("Introduza o nome do produto (ou 'sair' para terminar): ")
    if nome.lower() == 'sair':
        break
    preco = float(input("Introduza o preço: "))
    categoria = input("Introduza a categoria: ")
    
    produtos.append({"nome": nome, "preco": preco, "categoria": categoria})
    precos.append(preco)

if not produtos:
    print("Nenhum produto registado.")
else:
    # Filtragem por Preço[cite: 1]
    valor_filtro = float(input("\nFiltrar produtos com preço acima de: "))
    produtos_filtrados = [p for p in produtos if p["preco"] > valor_filtro]

    # Ordenação de produtos[cite: 1]
    precos_crescente = precos.copy()
    precos_crescente.sort() # Exibição por ordem crescente utilizando sort()[cite: 1]
    
    precos_decrescente = sorted(precos, reverse=True) # Exibição por ordem decrescente[cite: 1]

    # Conjunto de Categorias Únicas[cite: 1]
    categorias_unicas = set(p["categoria"] for p in produtos)

    # Tupla de Estatísticas contendo o menor preço, maior preço e média[cite: 1]
    estatisticas = (min(precos), max(precos), sum(precos) / len(precos))

    # Relatório Final Formatado utilizando f-strings[cite: 1]
    print("\n--- Relatório Final ---")
    print(f"Total de produtos registados: {len(produtos)}")
    print(f"\nProdutos com preço superior a {valor_filtro}€:")
    for p in produtos_filtrados:
        print(f"  - {p['nome']}: {p['preco']:.2f}€ (Categoria: {p['categoria']})")

    print(f"\nPreços por ordem crescente: {precos_crescente}")
    print(f"Preços por ordem decrescente: {precos_decrescente}")
    
    print(f"\nCategorias únicas encontradas: {categorias_unicas}")
    
    print(f"\nEstatísticas dos Preços:")
    print(f"  - Menor preço registado: {estatisticas[0]:.2f}€")
    print(f"  - Maior preço registado: {estatisticas[1]:.2f}€")
    print(f"  - Preço médio: {estatisticas[2]:.2f}€")