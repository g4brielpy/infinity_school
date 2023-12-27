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


# função remover aluno
def RemoverAluno():
    print('REMOVER ALUNO')
    # validar número da matrícula
    while True:
        # entrada da matrícula para remover
        matricula_del = str(input('Matrícula do aluno que sejá removido: '))
        if matricula_del.isdigit():
            break
        else:
            print('Valor inválido, digite apenas número\n')

    # busca matrícula na lista
    valor_encontrado = False
    for dicionario_aluno in lista_alunos:

        # iterar sobre cada dicionário separadamente
        for chave_aluno, valor_aluno in dicionario_aluno.items():

            if chave_aluno == matricula_del:
                # chaver e valor que será removido
                matricula_del = dicionario_aluno
                # valor(nome) que será removido
                nome_removido = valor_aluno
                # marcando que o valor foi localizado
                valor_encontrado = True
    
    # removendo caso seja encontrado
    if valor_encontrado == True:
        print(f'Aluno {nome_removido} removido')
        lista_alunos.remove(matricula_del)
    else:
        print('Aluno não encontrado')


# função exibir lista de alunos
def Exibir_Aluno():
    print(lista_alunos)