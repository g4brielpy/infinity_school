'''
8)Imprimindo argumentos de palavra-chave de uma função criada com Kwargs
'''

dados = {
    'nome': 'Gabriel',
    'idade': 18,
    'endereço': 'Belo Horizonte'
}

def imprimir_valores(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

imprimir_valores(**dados)