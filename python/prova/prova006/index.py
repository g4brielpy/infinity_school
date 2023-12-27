from moduloAluno import (
    AdicionarAluno
)

# Menu principal
while True:
    print('\n MENU DE ALUNOS')
    print('~ '*8)
    print(' ')
    print('[1] - Adicionar Aluno')
    print('[2] - Remover Aluno')
    print('[3] - Atualizar Aluno')
    print('[4] - Lista de Alunos')
    comando = str(input('COMANDO: '))

    # estrutura de chamada de módulo
    match comando:
        case '1':
            AdicionarAluno()
        # case '2':
            # Função
        # case '3':
            # Função
        # case '4':
            # Função
        case '5':
            break
        case _:
            print('Valor inválido')