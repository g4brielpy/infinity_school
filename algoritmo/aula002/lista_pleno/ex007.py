print('Dias da semana')
dia = int(input('Digite um número: '))

match dia:
    case 1:
        print('domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sábado')
    case _:
        print('Valor Invalido!')