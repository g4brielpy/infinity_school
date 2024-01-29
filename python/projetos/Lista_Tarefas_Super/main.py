'''
Desenvolver um programa de linha de comando que permite
aos usuários gerenciar suas tarefas diárias, atribuindo-lhes
prioridades e categorias. O projeto será organizado em várias
partes e usará funções, listas, tuplas, dicionários, conjuntos e
um ambiente virtual. 
'''

from tarefa import Tarefa

my_tarefas = Tarefa("", "", "", "")
MENU = f'''\nMENU TAREFAS
[1] - Criar Nova Tarefa
[2] - Listar Tarefas
[3] - Listar Tarefas por Categoria/Prioridade
[4] - Remover Tarefa
[5] - Marca Tarefa Como Concluida
[Q] - Sair
=> '''

while True:
    command = str(input(MENU))
    match command:
        case '1':
            nome_tarefa = input('Nome da tarefa: ')
            descricao_tarefa = input('Descrição da tarefa: ')
            while True:
                prioridade_tarefa = input(
                    'Prioridade da tarefa [A, M, B]: '
                ).upper()
                if prioridade_tarefa in ['A', 'M', 'B']:
                    break
                else:
                    print('Valor inválido!')
            categoria_tarefa = input('Categoria da tarefa: ')
            minha_tarefas = Tarefa(
                nome_tarefa, descricao_tarefa, prioridade_tarefa, categoria_tarefa
            )

        case '2':
            # print(my_tarefas.lista_de_tarefas)
            my_tarefas.exibir_tarefas()

        case '4':
            nome_deletar = input('Excluir tarefa de nome: ')
            my_tarefas.excluir_tarefa(nome_deletar)

        case 'q':
            print('PROGRAMA FINALIZADO')
            break
