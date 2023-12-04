numero = input('Informe um número: ')

if ('.' in numero):
    print(f'O número {numero} é um valor real')
elif ('.' not in numero):
    print('O número digitado é um valor inteiro')
else:
    print('Valor invalido')