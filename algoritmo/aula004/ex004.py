user = 'gabriel'
senha = '123'

user_input = str('')
senha_input = str('')
login = False

while (login != True):
    user_input = str(input('\nDigite seu user: '))
    senha_input = str(input('Digite sua senha: '))

    if (user_input == user) and (senha_input == senha):
        print('\nEntrou')
        login = True
    else:
        print('\nValor errado')

    