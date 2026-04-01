#Bibliotécas
import subprocess
import os

#Funções
def executar_comando(comando_prompt):
    try:
        resultado = subprocess.run(comando_prompt, shell=True)
    except Exception as e:
        print("Ocorreu um erro",e)
def ping_ip():
    executar_comando("ping 8.8.8.8")
def calculadora():
    executar_comando("calc")
def painel_controle():
    executar_comando("control panel")
def criar_pasta():
    pasta = str(input("Digite o nome da pasta: "))
    executar_comando(f"mkdir C:\{pasta}")
    print("Pasta Criada!") 
def traçar_ip():
    executar_comando("tracert 8.8.8.8")

#Menu de Escolhas
def menu():
    while True:
        print("Comandos do Prompt")
        print("1 - Ping IP")
        print("2 - Calculadora")
        print("3 - Painel de Controle")
        print("4 - Criar Pasta")
        print("5 - Traçar IP")
        print("6 - Sair")
        opcao = str(input("Escolha um dos números referente a uma das opções: "))

#Casos
        match opcao:
            case "1":
                ping_ip()
            case "2":
                calculadora()
            case "3":
                painel_controle()
            case "4":
                criar_pasta()
            case "5":
                traçar_ip()
            case "6":
                print("Saindo.")
            case _:
                print("Erro.")
if __name__ == "__main__":
    menu()