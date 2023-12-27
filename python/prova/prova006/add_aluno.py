# variáveis
aluno = dict()
lista_alunos = list()

# função adicionar alunos
def AdicionarAluno():
    print('ADICIONAR ALUNO')
    # validar núumero de matrícula
    while True:
        matricula_input = str(input('Matrícula do aluno: '))
        if matricula_input.isdigit():
            break
        else:
            print('Valor inválido, digite apenas número')

    nome_input = str(input('Nome do aluno:'))