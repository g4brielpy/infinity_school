# Calculadora usando módulos
import operacoes

# menu
while True:
    print('\nCALCULADORA')
    print('Qual operação deseja fazer')
    print('[1] - Soma')
    print('[2] - Subtrair')
    print('[3] - Multiplicar')
    print('[4] - Dividir')
    comando = str(input('COMANDO: '))

    match comando:
        case '1':
            operacoes.soma()
        case '2':
            operacoes.subtrair()
        case '3':
            operacoes.multiplicacao()
        case '4':
            operacoes.divisao()
        case '5':
            break
        case _:
            print('Valor inválido')