from moduloAluno import (
    AdicionarAluno,
    RemoverAluno,
    Exibir_Aluno,
    AtualizarAluno
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
    print('[5] - Exit')
    comando = str(input('COMANDO: '))
    print(' ')

    # estrutura de chamada de módulo
    match comando:
        case '1':
            AdicionarAluno()
        case '2':
            RemoverAluno()
        case '3':
            AtualizarAluno()
        case '4':
            Exibir_Aluno()
        case '5':
            break
        case _:
            print('Valor inválido')
