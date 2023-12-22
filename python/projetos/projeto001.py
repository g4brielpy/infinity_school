# nome, descrição, prioridade e categoria.

# VARIÁVEIS
Lista_Tarefas = list()


# FUNÇÕES TAREFAS
def add_tarefa():
    # valida nome
    while True:
        nome_input = str(input('Nome da Tarefa: '))
        
        if nome_input.isalpha():
            break
        else:
            print('Valor invalido')
    
    descricao_input = str(input('Descrição da Tarefa: '))
    
    # valida prioridade
    while True:
        prioridade_input = str(input('Prioridade [A - alta] [M - média] [B - baixa]: ').upper())

        if (prioridade_input == 'A') or (prioridade_input == 'M') or (prioridade_input == 'B'):
            break
        else:
            print('Valor invalido')

    categoria_input = str(input('Categoria: '))


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

add_tarefa()