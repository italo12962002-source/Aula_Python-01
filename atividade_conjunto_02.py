cliente_01  = {"Banana","Maça", "Pera","Pão","Carne","Arroz","Peixe","Banana"}
cliente_02 = {"Pão","Peixe","Batara","Refri","Chiclete"}
cliente_03 = {"Cane","Batata","Maça","Chiclete","Pipoca","Feijão","Peixe"}
cliente_04 = {"Banana","Peixe","Laranja","Café","Frango","Alface"}

itens_cliente_01 =set(cliente_01)
itens_cliente_02 =set(cliente_02)
itens_cliente_03 =set(cliente_03)
itens_cliente_04 =set(cliente_04)

#Não repete (SET)
print(f"Lista de itens do primeiro cliente: {itens_cliente_01}")
print(f"Lista de itens do segundo cliente: {itens_cliente_02}")
print(f"Lista de itens do terceiro cliente: {itens_cliente_03}")
print(f"Lista de itens do quarto cliente: {itens_cliente_04}")

#Itens em Comum (INTERSECTION)
itens_iguais = itens_cliente_01.intersection(itens_cliente_02)
print(f"\nItens iguais dos participantes: {itens_iguais}")

#Listagem de todos os itens (UNION)
todos_itens = itens_cliente_01.union(itens_cliente_02,itens_cliente_03,itens_cliente_04)
print(f"\nLista de Todos os Itens: {todos_itens}")

#Contagem de Todos os itens (LEN)
print(f"\nQuantidade de Itens: {len(todos_itens)}")