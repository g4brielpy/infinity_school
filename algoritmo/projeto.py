# Desenvolver um sistema de
# cadastro e confirmação de senha
# para usuário de smartphone.

while True:
    user_input = str(input('Digite seu User: '))
    senha_input = str(input('Digite sua Senha: '))
    senha_confirmar = str(input('Confirme sua Senha: '))

    if (senha_input == senha_confirmar):
        break
    else:
        print('Valor incorreto')
        print('Digite novamente!\n')