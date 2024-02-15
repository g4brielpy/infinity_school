'''
1) Soma de todos os argumentos:
Escreva uma função chamada soma_args que aceita um número variável de argumentos e retorna a soma de todos eles.
'''

def soma_args(*args):
    numeros = list(args)
    resultado = sum(numeros)
    return resultado

print(soma_args(1,5,6,4,8,))