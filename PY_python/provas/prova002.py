'''
Escreva um programa em Python que receba duas listas como entrada do usuário e retorne uma tupla contendo os elementos em comum entre as duas listas e a soma desses elementos.

Exemplo: 
    Se a entrada do usuário for: Lista 1: [2, 4, 6, 8] Lista 2: [1, 2, 3, 4, 5, 6] O programa deve retornar: ([2, 4, 6], 12)
'''

conjunto = list()
tupla = tuple()

lista1 = input('Digite os itens da lista 1 separados por espaço: ')
lista1 = list(lista1.split())

lista2 = input('Digite os itens da lista 2 separados por espaço: ')
lista2 = list(lista2.split())

lista2 = list(map(lambda x: int(x), lista2))
lista1 = list(map(lambda x: int(x), lista1))

for i in lista1:
    if i in lista2:
        conjunto.append(i)

soma = sum(conjunto)

tupla = (conjunto, soma)

print(f'Os valores repetidos e soma são: {tupla}')
