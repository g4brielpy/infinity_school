'''
módulo contendo todas as funções do modal
'''


def fazer_login(email_entrada, senha_entrada, login):
    email = email_entrada.get()
    senha = senha_entrada.get()

    # validação para fazer login
    if '@' in email and len(senha) > 6:
        login.configure(text='Login efetuado com sucesso!')
    else:
        if '@' not in email and len(senha) <= 6:
            login.configure(text='E-mail e Senha inválido')
        elif '@' not in email:
            login.configure(text='E-mail inválido')
        elif len(senha) <= 6:
            login.configure(text='Senha inválida')
