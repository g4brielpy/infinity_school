# variáveis
lista_alunos = list()
aluno = dict()

# função adicionar alunos
def AdicionarAluno():
    print('ADICIONAR ALUNO')
    # validar núumero de matrícula
    while True:
        # entrada da matrícula
        matricula_input = str(input('Matrícula do aluno: '))
        if matricula_input.isdigit():
            break
        else:
            print('Valor inválido, digite apenas número\n')
    # entrada do nome
    nome_input = str(input('Nome do aluno: '))

    # adicionando aluno em um dicionário, com matrícula de {chave}
    aluno = {
        matricula_input: nome_input,
    }
    # adicionando à lista de alunos
    lista_alunos.append(aluno)
    print(lista_alunos)
