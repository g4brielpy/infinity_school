'''
Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.

O programa deve fornecer as seguintes funcionalidades:

Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário. OK

Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula. OK

Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.

O programa deve ser executado em um loop contínuo até que o usuário escolha sair.
'''
dados_alunos = dict()
lista_alunos = dict()
contidade_alunos = 0
opcao = 1

print('\nCADASTRO DE ALUNOS')
print('-- '*7)
while True:
    print('\nAdicionar um aluno = 1')
    print('Remover um aluno = 2')
    print('Visualizar lista de alunos cadastrados = 3')
    opcao = int(input('Digite a opção desejada: '))
    print('\n')

    # solicitação do nome e matrícula
    aluno = str(input('Digite o Nome do aluno: ').title())
    while True:
        matricula = str(input(f'Digite a Matrícula do {aluno}: '))
        if matricula.isdigit():
            matricula = int(matricula)
            break
        else:
            print('valor inválido!')
    
    # add aluno no dicionário
    dados_alunos = {
        matricula: aluno
    }
    lista_alunos[matricula] = aluno
    contidade_alunos += 1

    # remover um aluno
    remover = str(input('Deseja remover algum aluno [S / N]: ').upper())
    if (remover == 'S'):
        matricula_remover = str(input('Digite a matricula do aluno que será removido: '))
        if matricula_remover.isdigit():
            matricula_remover = int(matricula_remover)
        else:
            print('valor inválido!')

        lista_alunos.pop(matricula_remover, None)

    # visualizar alunos
    print('Alunos existentes')
    print('-- '*7)
    for i in lista_alunos:
        print(f'Aluno: {lista_alunos[i]}; Matrícula: {i}')