# número da tabuáda WHILE
numb = int(input('\nDigite o número que deseje ver a tabuada de 1 até 10: '))
i = int(1)
print('-- '*5)

# estrutura da tabuada
if (numb >= 1) and (numb <= 10):
    while (i <= 10):
        soma = (numb * i)
        print(f'{numb} X {i} = {soma}')
        i += 1
    else:
        print('-- '*5)
        print(f'Tabuada do número {numb}\n')
else:
    print('Valor inválido!')