valor_par = []
valor_impar = []
for i in range(1, 6):
    numb = int(input(f'Digite o {i}° valor:'))

    if (numb % 2 == 0):
        if (numb == 0):
            continue
        valor_par.append(numb)
    else:
        valor_impar.append(numb)

print(f'O valores pares são: {valor_par}')
print(f'Os valores ímpares são: {valor_impar}')
