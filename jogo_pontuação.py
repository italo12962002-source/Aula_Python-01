# Criação do Dicionário de Jogos
pontos = {}

# Entrada de Jogadores
for x in range(5):
    nome = input(f"Informe o nome do {x+1}° jogador: ")
    pontuacao = int(input(f"Informe os pontos iniciais do {x+1}° jogador: "))

    pontos[nome] = pontuacao

# Mostrar jogadores cadastrados
print("\nLista de jogadores:")
for nome, pontuacao in pontos.items():
    print(f"{nome} - {pontuacao}")

# Subtração de pontos
nome_jogador = input("\nInforme o nome do jogador: ")
quantidade_pontos = int(input("Informe a quantidade de pontos: "))

# Verificação
if nome_jogador in pontos:
    pontos[nome_jogador] += quantidade_pontos
    print(f"\nNova pontuação de {nome_jogador}: {pontos[nome_jogador]}")
else:
    print("\nJogador não encontrado.")