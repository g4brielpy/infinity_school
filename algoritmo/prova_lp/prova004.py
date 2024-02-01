'''
Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
'''

lista_de_numeros = []

print('\nSOMA E MÉDIA\n')
while True:
    numero = float(input('Digite um número, ou "0" para encerrar: '))
    if numero == 0:
        break
    lista_de_numeros.append(numero)

soma = sum(lista_de_numeros)
quantidade = len(lista_de_numeros)
media = soma / quantidade

print(f'''
Soma: {soma}
Quantidade de números: {quantidade}
Média: {media:.2f}
''')
