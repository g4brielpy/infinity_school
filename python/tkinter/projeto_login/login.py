'''
módulo contendo todas as funções do modal
'''


def fazer_login(email_entrada, senha_entrada):
    email = email_entrada.get()
    senha = senha_entrada.get()

    # validação para fazer login
    if '@' in email and len(senha) > 6:
        print('Login efetuado com sucesso!')
    else:
        if '@' not in email:
            print('Email inválido!')
        if len(senha) <= 6:
            print('Senha inválida!')
