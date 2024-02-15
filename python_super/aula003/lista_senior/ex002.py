'''
Dado o seguinte dicionario:
meu_dicionario = {
    frutas_lista: [maçã, banana, laranja],
    numeros_tupla: (1, 2, 3),
    cores_lista: [vermelho, verde, azul],
    pontos_tupla: (5, 10, 15),
    nomes_lista: [Alice, Bob, Carol],
    coordenadas_tupla: ((1, 2), (3, 4), (5, 6))
}
Exiba na tela cada valor deste dicionario.
'''

meu_dicionario = {
    'frutas_lista': ['maçã', 'banana', 'laranja'],
    'numeros_tupla': (1, 2, 3),
    'cores_lista': ['vermelho', 'verde', 'azul'],
    'pontos_tupla': (5, 10, 15),
    'nomes_lista': ['Alice', 'Bob', 'Carol'],
    'coordenadas_tupla': ((1, 2), (3, 4), (5, 6))
}

for chave, lista in meu_dicionario.items():
    if type(lista) in [list, tuple, set]:
        for valor in lista:

            if type(valor) in [list, tuple, set]:

                for i in valor:
                    print(i)
                continue

            print(valor)
