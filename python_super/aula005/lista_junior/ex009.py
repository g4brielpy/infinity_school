'''
9)Crie uma função que retorne um dicionario formado por nome, idade e cpf com os dados que o usuario passar via input antes da chamada da função
'''

def user_dic(**kwargs):
    return kwargs

nome_input = input('Digite seu nome: ')
idade_input = int(input('Digite sua idade: '))
cpf_input = input('Digite seu cpf: ')

dado = user_dic(Nome=nome_input, Idade=idade_input, Cpf=cpf_input)

print(dado)

