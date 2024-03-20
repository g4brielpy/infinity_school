'''
Desenvolver um programa de linha de comando que permite
aos usuários gerenciar suas tarefas diárias, atribuindo-lhes
prioridades e categorias. O projeto será organizado em várias
partes e usará funções, listas, tuplas, dicionários, conjuntos e
um ambiente virtual. 
'''

from tarefa import Tarefa

from time import sleep
from termcolor import colored
from os import system

my_tarefas = Tarefa("", "", "", "")
MENU = f'''\nMENU TAREFAS
[1] - Criar Nova Tarefa
[2] - Listar Tarefas
[3] - Buscar Tarefas por Categoria
[4] - Buscar Tarefas por Prioridade
[5] - Remover Tarefa
[6] - Marca Tarefa Como Concluida
[Q] - Sair
=> '''

while True:
    sleep(1)
    command = str(input(MENU))
    system('cls')

    match command.lower():
        case '1':
            while True:
                print(colored(f'Criar Tarefa\n', 'blue'))
                nome_tarefa = input('Nome da tarefa: ').strip()
                if not nome_tarefa:
                    print(colored('Valor inválido, digite um nome para a tarefa.', 'red'))
                    sleep(1)
                    continue
                nome_valido = my_tarefas.verificar_nome(nome_tarefa)

                if nome_valido:
                    break
                else:
                    print(colored('Já existe uma tarefa com este nome.', 'red'))
                    sleep(1)

            descricao_tarefa = input('Descrição da tarefa: ')

            while True:
                prioridade_tarefa = input(
                    'Prioridade da tarefa [Alta, Media, Baixa]: ').title()

                if prioridade_tarefa in ['Alta', 'Media', 'Baixa']:
                    break
                else:
                    print(colored('Valor inválido!', 'red'))
                    sleep(1)

            categoria_tarefa = input('Categoria da tarefa: ')

            try:
                minha_tarefa = Tarefa(
                    nome_tarefa, descricao_tarefa, prioridade_tarefa, categoria_tarefa
                )
                print(colored('Tarefa criada com sucesso!', 'green'))
                sleep(1.5)
            except (ValueError,TypeError) as e:
                print(colored(f"Erro ao criar tarefa: {e}", 'red'))
                sleep(1)

        case '2':
            print(colored(f'Exibir Tarefas', 'blue'))
            print(my_tarefas.exibir_tarefas())
            sleep(2)

        case '3':
            print(colored(f'Exibir Tarefas Por Categoria\n', 'blue'))
            categoria_exibir = input('Exibir qual categoria de tarefas: ')
            print(my_tarefas.exibir_tarefas_categoria(categoria_exibir))
            sleep(2)

        case '4':
            print(colored(f'Exibir Tarefas Por Prioridade\n', 'blue'))
            prioridade_exibit = input(
                'Exibir qual prioridade de tarefas: ').title()
            print(my_tarefas.exibir_tarefa_prioridade(prioridade_exibit))
            sleep(2)

        case '5':
            print(colored(f'Excluir Tarefa\n', 'blue'))
            nome_deletar = input('Excluir tarefa de nome: ')
            print(my_tarefas.excluir_tarefa(nome_deletar))
            sleep(1.5)

        case '6':
            while True:
                tarefa_concluida = input('Nome da tarefa concluida: ').strip()
                if not tarefa_concluida:
                    print(colored('Valor inválido, digite o nome da tarefa.', 'red'))
                    sleep(1)
                    continue

                tarefa_valida = my_tarefas.verificar_nome(tarefa_concluida)

                if not tarefa_valida:
                    print(my_tarefas.concluir_tarefa(tarefa_concluida))
                    sleep(1.5)
                else:
                    print(colored(f'Tarefa {tarefa_concluida} não existe.', 'red'))
                    sleep(1)
                break

        case 'q':
            print(colored('PROGRAMA FINALIZADO', 'blue'))
            break

        case _:
            print(colored('Opção inválida, por favor, escolha novamente.', 'red'))
            sleep(1)
