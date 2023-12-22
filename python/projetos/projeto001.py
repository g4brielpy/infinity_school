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
    print(f'Tarefa ({nome_input}) adicionada.')


def del_tarefa():
    nome_tarefa_del = str(input('Qual a tarefa que deseja remove: '))
    


# MENU DE COMANDOS
print('\n  MENU PRINCIPAL')
print('~~~~~~~~~~~~~~~~~~')
print('[1] - Add Tarefa')
print('[2] - Del Tarefa')
print('[3] - Lista de Tarefas')
print('[4] - Tarefas por Prioridade')
print('[5] - Exit')
comando = str(input('COMANDO: '))
print(' ')



print(Lista_Tarefas)