'''
5)Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
'''

numeros = []
par = []
impar = []

for i in range(0, 19):
    numero = int(input('Digite um número inteiro: '))
    numeros.append(numero)
    
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'Números gerais: {numeros}')
print(f'Números pares: {par}')
print(f'Números impares: {impar}')