
while True:
    pc=int(input("Veja as opções disponiveis para computadores: \n1 - Computador Gamer \n2 - Computador Empresárial \n3 - Computador Doméstico \n4 - Computador Infantil \nEscolha um número referente a uma das quatro opções de computadores que temos disponiveis para computadores:"))

    match pc:
        case 1:
            print("======= Computador Game =======  \nCPU: Ryzen 5 \nGPU: RTX 4060 \nRAM: 16GB DDR4 \nArmazenamento: 1TB SSD NVMe \nFonte: 600W ")
            break
        case 2:
            print("======= Computador Empresárial =======  \nCPU: Intel Core i5 \nGPU: Intel UHD \nRAM: 16GB DDR4 \nArmazenamento: 500GB SSD NVMe \nFonte: 600W ")
            break
        case 3:
            print("======= Computador Doméstico =======  \nCPU:  Intel Core i3 \n GPU: Intel UHD 770 \nRAM: 8GB DDR3 \nArmazenamento: 500GB HD \nFonte: 500W ")
            break
        case 4:
            print("======= Computador Infantil =======  \nCPU:  Intel Core i3 \n GPU: Intel UHD 770 \nRAM: 8GB DDR3 \nArmazenamento: 256GB HD \nFonte: 500W ")
            break
        case _:
            print("\nOpção invalida! Escolha novamente um número que represente um dos quatro computadores disponiveis.\n")
 