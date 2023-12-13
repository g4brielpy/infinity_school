import random

x = random.randint(1, 100)
tentativas = 1

print('\nADIVINHE O NÚMERO\n')

while True:
    numb_input = int(input('Digite o número: '))
    if (numb_input != x):
        print('Valor errado!')
        print('Tente novamente')
        tentativas += 1
        if (numb_input > x):
            print('Número maior que o valor a ser adivinhado\n')
        else:
            print('Número menor que o valor a ser adivinhado\n')

    else:
        break

print(f'\nParabéns, o valor erá {x}')
print(f'Número de tentativa: {tentativas}')