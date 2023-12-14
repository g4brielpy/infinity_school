dados_alunos = dict()
lista_alunos = dict()
contidade_alunos = 0
opcao = 1

print('\nCADASTRO DE ALUNOS')
print('-- '*7)
while True:
    print('\nPAINEL DE ALUNOS\n')
    print('Adicionar um aluno = 1')
    print('Remover um aluno = 2')
    print('Lista de alunos cadastrados = 3')
    print('Exit = 4')
    opcao = int(input('Digite a opção desejada: '))
    print('-- '*7, '\n')

    match opcao:
        case 1:
        # solicitação do nome e matrícula
            print('CADASTRAR ALUNO')
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

        case 2:
        # remover um aluno
            remover = str(input('Deseja remover algum aluno [S / N]: ').upper())
            if (remover == 'S'):
                print('REMOVER ALUNO')
                matricula_remover = str(input('Digite a matricula do aluno que será removido: '))
                if matricula_remover.isdigit():
                    matricula_remover = int(matricula_remover)
                else:
                    print('valor inválido!')

                lista_alunos.pop(matricula_remover, None)

        case 3:
        # visualizar alunos
            print('ALUNOS CADASTRADOS')
            for i in lista_alunos:
                print(f'Aluno: {lista_alunos[i]}; Matrícula: {i}')

        case 4:
        # finalizar o programa
            print('EXIT...\n')
            break

        case _:
        # caso nenhuma opção acima seja atendida
            print('valor inválido!')