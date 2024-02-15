'''
Exercício 1: Calculadora Simples

Aluno 1: Crie funções para realizar as operações de soma, subtração, multiplicação e divisão.
Aluno 2: Crie um menu para permitir ao usuário escolher qual operação realizar.
'''


def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y


MENU = '''Calculadora

[1] - Soma
[2] - Subtração
[3] - Multiplicação
[4] - Divisão
[q] - Sair
=> '''

while True:
    comando = input(MENU)

    match comando:
        case '1':
            num1 = float(input('Digite o primeiro valor: '))
            num2 = float(input('Digite o segundo valor: '))
            print(soma(num1, num2))
        case '2':
            num1 = float(input('Digite o primeiro valor: '))
            num2 = float(input('Digite o segundo valor: '))
            print(subtracao(num1, num2))
        case '1':
            num1 = float(input('Digite o primeiro valor: '))
            num2 = float(input('Digite o segundo valor: '))
            print(multiplicacao(num1, num2))
        case '1':
            num1 = float(input('Digite o primeiro valor: '))
            num2 = float(input('Digite o segundo valor: '))
            print(divisao(num1, num2))
        case 'q':
            print('Programa finalizado!')
            break
