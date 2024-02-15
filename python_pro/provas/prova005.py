'''
[PY-A05]Escreva uma função em Python que recebe uma lista de números inteiros e retorna a média aritmética dos valores.
'''

numeros = [5, 15, 20, 25]

def media_numerica(lista_de_numeros):
    media = sum(lista_de_numeros) / len(lista_de_numeros)
    return media

media = media_numerica(numeros)
print(f'A media da lista de número {numeros} é {media}')