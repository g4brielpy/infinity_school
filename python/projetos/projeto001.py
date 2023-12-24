# VARIÁVEIS

# Lista com todas as Tarefas criadas
Lista_Tarefas = list()

# Dicionário para criar uma Tarefas e atribuir ela a lista
Tarefas = dict()


# FUNÇÕES TAREFAS

def add_tarefa():

    # valida nome
    while True:
        nome_input = str(input('Nome da Tarefa: '))
        
        # verificar se valor é repetido
        for tarefa in Lista_Tarefas:
            if tarefa['nome'] == nome_input:
                print('Tarefa já existente')
                return
                
        if nome_input.isalpha():
            break
        else:
            print('Valor invalido')

    # coletar descrição do user (opç)
    descricao_input = str(input('Descrição da Tarefa: '))
    
    # valida prioridade
    while True:
        prioridade_input = str(input('Prioridade [A - alta] [M - média] [B - baixa]: ').upper())

        if prioridade_input in ('A', 'M', 'B'):
            match prioridade_input:
                case 'A':
                    prioridade_input = 'Alta'
                case 'M':
                    prioridade_input = 'Média'
                case 'B':
                    prioridade_input = 'Baixa'
            break
        else:
            print('Valor invalido')
    
    # coletar categoria do user (opç)
    categoria_input = str(input('Categoria: '))

    # Criando uma Tarefas
    Tarefas = {
        'nome': nome_input,
        'descrição': descricao_input,
        'prioridade': prioridade_input,
        'categoria': categoria_input,
    }
    # Adicionando a tarefa criada a lista
    Lista_Tarefas.append(Tarefas)
    print(f'TAREFA ({nome_input}) ADICIONADA.\n')


def del_tarefa():

    # verificar se a lista está vazia
    if Lista_Tarefas == []:
        print('Lista de Tarefa vazia')
        return

    # nome da tarefa para remover
    nome_tarefa_del = str(input('Qual a tarefa que deseja remove: '))
    lista_copia = Lista_Tarefas
    index_del = 0


    # verificando se a tarefa existe
    for tarefa in lista_copia:
        if nome_tarefa_del == tarefa['nome']:
            # removendo tarefa pelo index
            print(f'TAREFA: {Lista_Tarefas[index_del] ['nome']} Removido')
            Lista_Tarefas.pop(index_del)
            valor_localizado = True
            break
        else:
            valor_localizado = False
        index_del += 1

    # mensagem de aviso coso a tarefa não seja encontrada
    if (valor_localizado == False):
        print('Tarefa não encontrada')


def exibir_tarefas():

    # verificar se a lista está vazia
    if Lista_Tarefas == []:
        print('Lista de Tarefa vazia')
        return

    for tarefa in Lista_Tarefas:
        print('TAREFA')
        print(f'Nome: {tarefa["nome"]}')
        print(f'Descrição: {tarefa["descrição"]}')
        print(f'Prioridade: {tarefa["prioridade"]}')
        print(f'Categoria: {tarefa["categoria"]}\n')


def buscar_tarefa_prioridade():
    # verificar se a lista está vazia
    if Lista_Tarefas == []:
        print('Lista de Tarefa vazia')
        return
    
    # lista de tarefas da mesma prioridade
    Lista_Tarefas_Prioridade = list()
    
    # input para busca tarefa
    while True:
        tarefa_busca = str(input('Informe qual Prioridade de tarefa deseja buscar [A - alta] [M - média] [B - baixa]: ').upper())
        print(' ')

        if tarefa_busca in ('A', 'M', 'B'):
            match tarefa_busca:
                case 'A':
                    tarefa_busca = 'Alta'
                case 'M':
                    tarefa_busca = 'Média'
                case 'B':
                    tarefa_busca = 'Baixa'
            break
        else:
            print('Valor invalido')
        
    # buscar e armazenar tarefas
    for tarefa in Lista_Tarefas:
        if tarefa['prioridade'] == tarefa_busca:
            Lista_Tarefas_Prioridade.append(tarefa)

    # exibir tarefas
    for tarefa in Lista_Tarefas_Prioridade:
        print(f'TAREFA DE PRIORIDADE {tarefa_busca.upper()}')
        print(f'Nome: {tarefa["nome"]}')
        print(f'Descrição: {tarefa["descrição"]}')
        print(f'Prioridade: {tarefa["prioridade"]}')
        print(f'Categoria: {tarefa["categoria"]}\n')


def buscar_tarefa_categoria():
    # verificar se a lista está vazia
    if Lista_Tarefas == []:
        print('Lista de Tarefa vazia')
        return
    
    # lista de tarefas da mesma cartegoria
    Lista_Tarefas_categoria = list()

    tarefa_busca = str(input('Informe qual Categoria de tarefa deseja buscar: '))
    print(' ')

    # buscar e armazenar terefas
    for tarefa in Lista_Tarefas:
        if tarefa['categoria'] == tarefa_busca:
            Lista_Tarefas_categoria.append(tarefa)

    # verificar se algum valor foi encontrado
    if len(Lista_Tarefas_categoria) == 0:
        print('Categoria não encontrada')
        return

    # exibir tarefas
    for tarefa in Lista_Tarefas_categoria:
        print(f'TAREFA DE CATEGORIA {tarefa_busca.upper()}')
        print(f'Nome: {tarefa["nome"]}')
        print(f'Descrição: {tarefa["descrição"]}')
        print(f'Prioridade: {tarefa["prioridade"]}')
        print(f'Categoria: {tarefa["categoria"]}\n')



# MENU DE COMANDOS
while True:
    print('\n  MENU PRINCIPAL')
    print('~~~~~~~~~~~~~~~~~~')
    print('[1] - Add Tarefa')
    print('[2] - Del Tarefa')
    print('[3] - Lista de Tarefas')
    print('[4] - Tarefas por Prioridade')
    print('[5] - Tarefas por Categorias')
    print('[6] - Exit')
    comando = str(input('COMANDO: '))
    print(' ')
    match comando:
        case '1':
            add_tarefa()
        case '2':
            del_tarefa()
        case '3':
            exibir_tarefas()
        case '4':
            buscar_tarefa_prioridade()
        case '5':
            buscar_tarefa_categoria()
        case '6':
            break
        case _:
            print('Valor inválido! Digite novamente')