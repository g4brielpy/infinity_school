# Lista de valores pares e ímpares
lista_numero = []
valores_pares = []
valores_impares = []
i = 1

# solicitar os valores
while (i <= 10):
    numero = int(input(f'Digite o {i}° valor: '))
    lista_numero == lista_numero.append(numero)
    i += 1

# separar os valores pares e impares
for i in lista_numero:
    if (i % 2 == 0):
        valores_pares.append(i)
    else:
        valores_impares.append(i)

# transformando as listas pares e impares em Tuplas
valores_pares = tuple(valores_pares)
valores_impares = tuple(valores_impares)

# Exibindo os valores
print(f'\nOs valores pares são: {valores_pares}')
print(f'Os valores ímpares são: {valores_impares}\n')

# quantidade de números pares e ímpares
quantidade_par = len(valores_pares)
quantidade_impar = len(valores_impares)

print(f'A quantidade de números pares são: {quantidade_par}')
print(f'A quantidade de número ímpares são : {quantidade_impar}\n')

# soma dos valores da lista
soma_par = sum(valores_pares)
soma_impar = sum(valores_impares)
soma_total = sum(lista_numero)

print(f'A soma dos número pares são: {soma_par}')
print(f'A soma dos número ímpares são: {soma_impar}')
print(f'A soma total de todos os números são: {soma_total}\n')
