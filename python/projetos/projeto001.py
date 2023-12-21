# variáveis
lista_tarefas = list()
disc_tarefas = dict()
qtd_tarefas = 0

# funções taks

# adicionar tarefas: 
def add_tarefa():
    nome = str(input('Adicione uma o Nome da Tarefa: '))
    descricao = str(input('Qual a Descrição da Tarefa: '))
    prioridade = str(input('Digite a Prioridade da Tarefa: '))
    categoria = str(input('Digite a Categoria da Tarefa: '))

    disc_tarefas = {
        'nome': nome,
        'descrição': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
    }
    lista_tarefas.append(disc_tarefas)

# remover tarefas

# MENU
while True:
    # menu de comando
    print('\nMENU DE COMANDO:')
    print('-- '*6)
    print('Adicionar Tarefa = [ADD]')
    print('Remover Tarefa = [DEL]')
    print('Lista de Tarefas: [LISTA]')
    print(f'Quantidade de taferas: {qtd_tarefas}')
    comando = str(input('Comando: ').upper())
    match comando:
        case 'ADD':
            add_tarefa()
            qtd_tarefas += 1


