'''
3)Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

numeros = []

for i in range(0, 11):
    numero = float(input('Digite um numero: '))
    numeros.append(numero)

print('Ordem original')
print(numeros)

print('Ordem inversa')
print(numeros[::-1])