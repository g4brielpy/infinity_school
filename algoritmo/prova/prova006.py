valores = [ ]
iguai = [ ]
for i in range(1, 4):
    x = int(input(f'Digite o {i}° valor: '))

    if (x in valores):
        iguai.append(x)
        continue

    valores.append(x)

maior_valor = max(valores)
menor_valor = min(valores)

print(f'\nO maior valor é {maior_valor}')
print(f'O menor valor é {menor_valor}')
if (len(iguai) >= 1):
    print(f'Os valores iguais são {iguai}')
else:
    print('Não há valores iguais')