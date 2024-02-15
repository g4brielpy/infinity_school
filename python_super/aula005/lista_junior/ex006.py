'''
6)Ordenação de números: Escreva uma função chamada ordenar_numeros que aceita um 
número variável de argumentos e retorna uma lista ordenada desses números em ordem crescente
'''


def ordenar_numeros(*args):
    args = list(args)
    lista_ordenada = sorted(args)
    return lista_ordenada


numeros = (5, 8, 9, 2, 1, 12)
print(ordenar_numeros(*numeros))
