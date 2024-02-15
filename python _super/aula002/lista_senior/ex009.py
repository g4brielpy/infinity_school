'''
9)Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
'''

pessoa = []
lista_pessoas = []

for i in range(0, 3):
    print('\nPESSOA')
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite sua altura: '))

    pessoa = [idade, altura]
    lista_pessoas.append(pessoa)

# lista normal
print(lista_pessoas)

# inverter valor
print(lista_pessoas[::-1])