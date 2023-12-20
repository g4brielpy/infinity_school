# pytthon - super: aula 5 | função II

'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:


Função map() para obter uma nova lista com o quadrado de cada número da lista numeros

Função filter() para obter uma nova lista com números pares da lista numeros

Função reduce()  para obter a soma de todos os números da lista numeros

Qual o resultado obtido após a execução das operações acima?
'''
# lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# função map - quadrado de cada número da lista numeros
quadrado = list(map(lambda x: x **2, numeros))
print(f'O quadrado de cada número são: {quadrado}')

# função filter - nova lista com números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f'Os números pares são: {pares}')
