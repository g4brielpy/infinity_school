'''
Exercício 2: Conversor de Unidades

Aluno 1: Crie funções para converter entre diferentes unidades de medida, como Celsius para Fahrenheit, quilômetros para milhas, etc.
Aluno 2: Crie um menu que permite ao usuário escolher qual conversão realizar.
'''


def celsius_para_fahrenheit(celsius):
    temperatura_fahrenheit = (celsius * 9/5) + 32
    return temperatura_fahrenheit


def quilometros_para_milhas(km):
    distancia_milhas = km * 0.621371
    return distancia_milhas


MENU = '''Conversor de Unidades

[1] - Celsius para Fahrenheit
[2] - Quilômetros para Milhas
[q] - Sair
=> '''

while True:
    comando = input(MENU)

    match comando:
        case '1':
            celsius = float(input('Digite a temperatura em Celsius: '))
            fahrenheit = celsius_para_fahrenheit(celsius)
            print(f'A temperatura em Fahrenheit é: {fahrenheit:.2f}')

        case '2':
            quilometros = float(input('Digite a distância em quilômetros: '))
            milhas = quilometros_para_milhas(quilometros)
            print(f'A distância em milhas é: {milhas:.2f}')

        case 'q':
            print('Programa encerrado!')
            break

        case _:
            print('Valor inválido!')
