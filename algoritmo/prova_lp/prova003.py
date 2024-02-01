'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
'''

tabuada = int(input('\nExibir tabuada de qual número interio [1 a 10]: '))

if tabuada >= 1 and tabuada <= 10:
    print(f'\nTABUADA {tabuada}')
    for i in range(1, 11):
        print(f'{tabuada} X {i} = {tabuada * i}')
else:
    print('Valor inválido!')
