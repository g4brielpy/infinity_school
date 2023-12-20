# pytthon - super: aula 5 | função II

# import de funções
from functools import reduce

# lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# função map - quadrado de cada número da lista numeros
quadrado = list(map(lambda x: x **2, numeros))
print(f'\nO quadrado dos número são: {quadrado}')

# função filter - nova lista com números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f'Os números pares são: {pares}')

# função reduce - soma de todos os números
soma = int(reduce(lambda x, y: x + y, numeros))
print(f'A soma de todos os números são: {soma}\n')
