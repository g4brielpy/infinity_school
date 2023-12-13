'''
Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.

O programa deve fornecer as seguintes funcionalidades:

Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.

Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.

Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.

O programa deve ser executado em um loop contínuo até que o usuário escolha sair.
'''
print('CADASTRO DE ALUNOS')
while True:
    # solicitação do nome e matrícula
    aluno = str(input('Digite o Nome do aluno: ').title())
    while True:
        matricula = str(input(f'Digite a Matrícula do {aluno}: '))
        if matricula.isdigit():
            matricula = int(matricula)
            break
        else:
            print('valor inválido!')