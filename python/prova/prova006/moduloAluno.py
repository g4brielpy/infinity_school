# variáveis
lista_alunos = list()
aluno = dict()



# MÓDULOS

# função verificar lista vazia
def lista_valida():
    if len(lista_alunos) > 0:
        valido = True
        return valido
    else:
        valido = False
        print('ERRO: Lista Vazia')
        return valido
    


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
    valido = lista_valida()
    if not valido:
        return

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
    if valor_encontrado:
        print(f'Aluno {nome_removido} removido')
        lista_alunos.remove(matricula_del)
    else:
        print('Aluno não encontrado')



# função atualizar nome de aluno
def AtualizarAluno():
    valido = lista_valida()
    if not valido:
        return

    print('ATUALIZAR CADASTRO DE ALUNO')
    lista_alunos_atualizada = lista_alunos

    # validar número da matrícula
    while True:
        # entrada da matrícula para atualizar
        matricula_atualizar = str(input('Matrícula do aluno que sejá atualizado: '))
        if matricula_atualizar.isdigit():
            break
        else:
            print('Valor inválido, digite apenas número\n')
    
    # novo nome
    nome_input = str(input('Novo nome do aluno: '))

    # busca matrícula na lista
    valor_encontrado = False
    i = 0
    for dicionario_aluno in lista_alunos_atualizada:

        # iterar sobre cada dicionário separadamente
        for chave_aluno, valor_aluno in dicionario_aluno.items():
            if chave_aluno == matricula_atualizar:

                # atualizar nome
                dicionario_aluno[chave_aluno] = nome_input
                valor_encontrado = True

                # subir para lista original
                lista_alunos[i] = dicionario_aluno

        # atualizar index caso o valor não seja localizado
        i += 1

    # saída se o valor for encontrado
    if valor_encontrado:
        print('Valor alterado')
        print(f'Novo nome: {nome_input}')
    else:
        print('Valor não localizado')

                
        
# função exibir lista de alunos
def Exibir_Aluno():
    valido = lista_valida()
    if not valido:
        return

    for dicionario_aluno in lista_alunos:
        for chave_matricula, valor_nome in dicionario_aluno.items():
            print('\nALUNO')
            print(f'Nome: {valor_nome}')
            print(f'Matrícula: {chave_matricula}')
        