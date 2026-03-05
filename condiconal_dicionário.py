#Criação do Dicionário
aluno = {}
#Entrada de Dados
aluno["Nome"] =input("Digite o nome do aluno: ")
aluno["Nota"] =float(input("\nDigite a nota do aluno: "))
aluno["Curso"] =input("\nDigite o curso do aluno:")

#Saída de Dados
print(f"\nSegue dados do aluno:\nNome: {aluno["Nome"]} \nIdade: {aluno["Nota"]} \nCurso:{aluno["Curso"]}")
print(f"Situação do Aluno: Aprovado" if aluno["Nota"] >=18 else "Situação do Aluno: Reprovado")
