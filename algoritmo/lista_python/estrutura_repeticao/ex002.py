while True:
    nome = str(input('Digite seu nome de usuário: '))
    senha = str(input('Digite sua senha: '))

    if (nome == senha):
        print('ERRO: Senha não pode ser igual ao nome! \n')
    else:
        print('Acesso')
        break