'''
7)Soma dos quadrados dos números:
Escreva uma função chamada soma_quadrados que aceita um número variável de argumentos e retorna a 
soma dos quadrados de todos os números passados como argumentos.
'''
numeros = (1, 5, 8, 78, 415, 46,)
soma_quadrados = list(map(lambda x: x ** 2, numeros))

print(soma_quadrados)
