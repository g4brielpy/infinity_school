# login válido
email = str('userbh@gmail.com')
senha = str('user123')

email_input = str(input('Digite seu email: '))
senha_input = str(input('Digite sua senha: '))

erro = True
while (erro == True):
    # Email e Senha errados
    if (email_input != email) or (senha_input != senha):
        print('\nEmail e Senha errado')
        print('-- ' * 5,'\n')
        email_input = str(input('Digite seu email novamente: '))
        senha_input = str(input('Digite sua senha novamente: '))
    else:
        print('\nAcesso liberado')
        erro = False
