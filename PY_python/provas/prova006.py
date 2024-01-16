'''
[PY-A06]Considere o seguinte trecho de código em Python:

'import random

lista = [1, 2, 3, 4, 5]
x = random.choice(lista)'



a) Explique o que o código faz.
    resposta:
    1) O código importa a biblioteca 'random' do python. 
    2) cria uma 'list' de números inteiro e atribui na variável 'lista'.
    3) Atribui na variável 'x' um número aleatório da variável 'lista' utilizando o método 'choice' da biblioteca 'random'.

b) Escreva um trecho de código que use a função random para gerar um número inteiro aleatório entre 10 e 20 (inclusive).
c) Escreva um trecho de código que use a função random para gerar uma lista com 5 elementos inteiros aleatórios entre 1 e 100 (inclusive).
'''
import random

# b)
numero_aleatorio = random.randint(10, 20)
print(f'Número aleatório entre 10 e 20: {numero_aleatorio}')

# c)
lista_numeros_aleatorios = list()
for _ in range(5):
    numero = random.randint(1, 100)
    lista_numeros_aleatorios.append(numero)

print(f'Lista com 5 elementos inteiros aleatórios entre 1 e 100: {lista_numeros_aleatorios}')

