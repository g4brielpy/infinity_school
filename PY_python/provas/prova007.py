'''
[PY-A07]Você foi contratado para desenvolver um programa que calcule a média de notas dos alunos de uma turma. Para isso, você deverá criar uma lista com as notas de cada aluno e, em seguida, implementar uma função que calcule a média aritmética das notas. 
Além disso, você deverá utilizar um loop while para pedir ao usuário que insira as notas dos alunos até que ele decida parar. 
Por fim, você deverá utilizar um loop for para imprimir a média de cada aluno.
'''

cont = int(1)
mais_notas = bool(True)
aluno = bool(True)
alunos = dict()
notas = list()

while aluno:
    print(f'\nAluno {cont}')
    i = int(1)

    while mais_notas:
        # entrada das notas do usuário
        nota = float(input(f'Digite o valor da {i}° nota: '))
        notas.append(nota)
        i += 1

        # verificando se o usuário quer continuar
        while True:
            continuar = str(input('\nDeseja inserir mais notas [S/N]: '))
            # encerrando o loop
            if continuar.upper() == 'N':
                mais_notas = False
                break
            # adicionar mais notas
            elif continuar.upper() == 'S':
                break
            # valor inválido
            elif continuar.upper() not in ['S', 'N']:
                print('Valor inválido')

    # adicionar notas na chave do aluno
    notas_aluno = notas.copy()
    alunos[f'aluno {cont}'] = notas_aluno
    notas.clear()
    print(alunos)

    while True:
        aluno = str(input(f'\nDeseja cadastrar outro aluno [S/N]: '))

        # atualizando a quantidade de alunos
        if aluno.upper() == 'S':
            aluno = True
            mais_notas = True
            cont += 1
            break
        # encerrando o loop
        elif aluno.upper() == 'N':
            aluno = False
            break
        # valor inválido
        else:
            print('Valor inválido')
