import subprocess
import os

def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
        print("Erro ao executar o comando.",e)

def tracar_ip():
    executar_comando("tracert")

def calculadora():
    executar_comando("calc")

def desligar():
    executar_comando("shutdown")

def painel_controle():
    executar_comando("control panel")

def criar_pasta():
    pasta = str(input("Digite o nome da pasta: "))
    executar_comando(f"mkdir C:\{pasta}")
    print("Pasta Criada!") 

def bloco_de_notas():
    executar_comando("notepad")

def explorador_de_arquivos():
    executar_comando("explorer")

def data():
    executar_comando("date")

def info_sistema():
    executar_comando("systeminfo")

def gerenciador_de_tarefas():
    executar_comando("tasklist")

   

def menu():
    while True:
        print("========= Ferramentas Uteis =========")
        print("1 - Traçar IP")
        print("2 - Calculadora")
        print("3 - Desligar o Computador (Cuidado)")
        print("4 - Painel de Controle")
        print("5 - Criar Pasta")
        print("6 - Bloco de Notas")
        print("7 - Explorador de Arquivos")
        print("8 - Data")
        print("9 - Informações do Sistema")
        print("10 - Gerenciador de Tarefas ")
        print("0 - Sair")
        print("=========Criado por Italo=========")
        opcao = str(input("Escolha: "))

        match opcao:
            case "1":
                tracar_ip()
            case "2":
                calculadora()
            case "3":
                desligar()
            case "4":
                painel_controle()
            case "5":
                criar_pasta()
            case "6":
                bloco_de_notas()
            case "7":
                explorador_de_arquivos()
            case "8":
                data()
            case "9":
                info_sistema()
            case "10":
                gerenciador_de_tarefas()
            case "0":
                print("Saindo.")
                break
            case _:
                print("Erro.")
if __name__ == "__main__":
    menu()