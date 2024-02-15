''' 
1)Considere a seguinte lista de números: [2, 5, 8, 11, 14]. 
Escreva um programa que itere sobre essa lista e exiba cada número elevado ao quadrado.
'''

numeros = [2, 5, 8, 11, 14]
print(f'Numeros: {numeros}')

numeros_quadrado = list(map(lambda x: x **2, numeros))
print(f'Numeros ao quadrado: {numeros_quadrado}')