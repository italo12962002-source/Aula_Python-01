#Criação do Dicionário Estoque
estoque = {
    "Camisa" : 10,
    "Calça" : 15,
    "Coné" : 20,
    "Tenis" : 5

}

#Mostrar Estoque Atual
print("Estoque Atual")
for produto, quantidade in estoque.items():
    print(f"{produto}:{quantidade}")

#Entrada de Dados
nome_produto = input("\nInforme o nome do produto vendido: ")
quantidade_vendida = int(input("\nInforme a quantidade vendidada:"))

#Atualizar estoque
if nome_produto in estoque:
    if quantidade_vendida<= estoque[nome_produto]:
        estoque[nome_produto] = estoque[nome_produto] - quantidade_vendida
        print("Venda Realizada com Sucesso!")
else:
    print("produto não encontrado!")
for produto, quantidade in estoque.items():
    print(f"{produto} | {quantidade}")