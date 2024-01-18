'''
módulo contendo todas as funções do modal
'''


def fazer_login(email_entrada, senha_entrada):
    email = email_entrada.get()
    senha = senha_entrada.get()

    print('\nOlá, Mundo!')
    print(f'E-mail: {email}')
    print(f'Senha: {senha}')
