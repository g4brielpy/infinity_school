# variáveis
lista_tarefas = dict()
cont = 1

disc_tarefas = dict()
qtd_tarefas = 0


# FUNÇÕES TAKS

# adicionar tarefas: 
def add_tarefa(qtd_tarefas):
    # inputs para adicionar a lista

    nome = str(input('Adicione o Nome da Tarefa: '))
    # verificando se o usuário digitou um nome válido
    if not nome.isalpha():
        print('\nValor invalido')
        return qtd_tarefas
    
    # verificar se a tarefa já existe
    for chave, valor in lista_tarefas.items():
        # verificando o Sub Dicionário de cada tarefa
        if valor['nome'] == nome:
            print(f'\nO nome da Tarefa "{nome}" já existe. Acesse "ADD" e escolha outro!')
            return qtd_tarefas

    descricao = str(input('Qual a Descrição da Tarefa: '))
    prioridade = str(input('Digite a Prioridade da Tarefa: '))
    categoria = str(input('Digite a Categoria da Tarefa: '))
        
    # adicionando a tarefa
    disc_tarefas = {
        'nome': nome,
        'descrição': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
    }
    lista_tarefas[f'TAREFA ({nome.upper()})'] = disc_tarefas

    qtd_tarefas += 1
    return qtd_tarefas


# remover tarefas
def del_tarefa(qtd_tarefas):
    nome_del = str(input('Digite o NOME da Tarefa que deseja Remover: '))
    nome_del = str(f'TAREFA ({nome_del.upper()})')

    chaves_a_remover = []

    for chave, valor in lista_tarefas.items():
        if nome_del == chave:
            chaves_a_remover.append(chave)
        else:
            print('\nValor não encontrado')

    for chave in chaves_a_remover:
        lista_tarefas.pop(chave)
        print(f'\nTarefa "{chave}" removida com sucesso.')
        qtd_tarefas -= 1
        return qtd_tarefas


# MENU
while True:
    # menu de comando
    print('\n  MENU DE COMANDO:')
    print('-- '* 7)
    print('Adicionar Tarefa = [ADD]')
    print('Remover Tarefa = [DEL]')
    print('Lista de Tarefas: [LISTA]')
    print('Sair: [EXIT]')
    print(f'Quantidade de taferas: {qtd_tarefas}')
    comando = str(input('Comando: ').upper())
    match comando:
        case 'ADD':
            qtd_tarefas = add_tarefa(qtd_tarefas)
        case 'DEL':
            qtd_tarefas = del_tarefa(qtd_tarefas)
        case 'LISTA':
            print(lista_tarefas)
        case 'EXIT':
            break
        case _:
            print('\nValor inválido')

