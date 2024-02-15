'''
Exercício 4: Lista de Tarefas

Aluno 1: Crie funções para adicionar, listar e remover tarefas de uma lista.
Aluno 2: Crie um menu para permitir ao usuário interagir com a lista de tarefas.
'''

lista_tarefas = []


def adicionar_tarefas(nome, descricao):
    tarefa = dict()
    tarefa[nome] = descricao
    lista_tarefas.append(tarefa)
    return


def exibir_tarefas():
    i = 1
    for tarefa in lista_tarefas:
        print(i, tarefa)
        i += 1


def remover_tarefa(posicao):
    posicao = int(posicao) - 1
    lista_del = lista_tarefas.pop(posicao)
    chave_del = list(lista_del.keys())
    return f'Tarefa {chave_del[0]} foi removida!'


menu = '''Lista de Tarefas

[1] - Adicionar Tarefas
[2] - Listar e ver posições das Tarefas
[3] - Remover Tarefas
[4] - Sair
=> '''

while True:
    comando = input(menu)
    if comando == '1':
        nome = input('Nome da tarefa: ')
        descricao = input('Descrição da tarefa: ')
        adicionar_tarefas(nome, descricao)

    elif comando == '2':
        exibir_tarefas()

    elif comando == '3':
        posicao = input('Digite a posição da tarefa que quer remover: ')
        retorno = remover_tarefa(posicao)
        print(retorno)

    elif comando == '4':
        break
