menu = input("Você deseja confirmar? \n1 - Sim \n2 - Não \nEscolha um número referenrte a opção de confirmar sua escolha? ")

match menu:
    case "1":
        print("Confirmação feita!")
    case "2":
        print("Opção rejeitada!")
    case _:
        print("Opção invalida, escolha novamente uma das opções disponiveis.") 
