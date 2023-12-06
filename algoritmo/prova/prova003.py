# número da tabuáda
numb = int(input('\nDigite o número que deseje ver a tabuada de 1 até 10: '))
print('-- '*5)

# estrutura da tabuada
if (numb >= 1) and (numb <= 10):
    for i in range(1, 11):
        soma = (numb * i)
        print(f'{numb} X {i} = {soma}')
    else:
        print('-- '*5)
        print(f'Tabuada do número {numb}\n')
else:
    print('Valor inválido!')