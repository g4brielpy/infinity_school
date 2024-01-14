'''
Solicite ao usuario se o numero de chaves que deseja no seu dicionario e faça um
programa que crie este dicionario de acordo com as informções que o usuario
colocar no programa. chave:valor
'''

dicionario = dict()
quantidade_itens = int(input('Qual a quantidade de itens do dicionário [chave: valor]: '))

for i in range(quantidade_itens):
    chave = str(input('Chave: '))
    valor = str(input('Valor: '))
    print('Valor adicionado\n')

    dicionario[chave] = valor

print(dicionario)