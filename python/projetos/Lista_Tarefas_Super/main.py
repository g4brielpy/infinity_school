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
[3] - Buscar Tarefas por Categoria
[4] - Buscar Tarefas por Prioridade
[5] - Remover Tarefa
[6] - Marca Tarefa Como Concluida
[Q] - Sair
=> '''

while True:
    command = str(input(MENU))

    match command.lower():
        case '1':
            while True:
                nome_tarefa = input('Nome da tarefa: ').strip()
                if not nome_tarefa:
                    print('Valor inválido, digite um nome para a tarefa.')
                    continue
                nome_valido = my_tarefas.verificar_nome(nome_tarefa)

                if nome_valido:
                    break
                else:
                    print('Já existe uma tarefa com este nome.')

            descricao_tarefa = input('Descrição da tarefa: ')

            while True:
                prioridade_tarefa = input(
                    'Prioridade da tarefa [Alta, Media, Baixa]: ').title()

                if prioridade_tarefa in ['Alta', 'Media', 'Baixa']:
                    break
                else:
                    print('Valor inválido!')

            categoria_tarefa = input('Categoria da tarefa: ')

            try:
                minha_tarefa = Tarefa(
                    nome_tarefa, descricao_tarefa, prioridade_tarefa, categoria_tarefa
                )
                print('Tarefa criada com sucesso!')
            except ValueError as e:
                print(f"Erro ao criar tarefa: {e}")

        case '2':
            print(my_tarefas.exibir_tarefas())

        case '3':
            categoria_exibir = input('Exibir qual categoria de tarefas: ')
            print(my_tarefas.exibir_tarefas_categoria(categoria_exibir))

        case '4':
            prioridade_exibit = input('Exibir qual prioridade de tarefas: ')
            print(my_tarefas.exibir_tarefa_prioridade(prioridade_exibit))

        case '5':
            nome_deletar = input('Excluir tarefa de nome: ')
            print(my_tarefas.excluir_tarefa(nome_deletar))

        case 'q':
            print('PROGRAMA FINALIZADO')
            break

        case _:
            print('Opção inválida, por favor, escolha novamente.')
