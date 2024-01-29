'''
4)Verificação de argumentos pares:
Escreva uma função chamada verifica_pares que aceita um número variável de argumentos e retorna uma lista contendo apenas os argumentos pares.
'''

def verifica_pares(*args):
    pares = []

    for valor in args:
        if valor % 2 == 0:
            pares.append(valor)

    return f'Os valores pares são: {pares}'