idade = int(input('Informe sua idade: '))
responsavel = str(input('Está acompanhado dos seus pais [s / n]: '))

if (idade >= 18):
    print('Usuário pode entrar')
elif (responsavel == 's'):
    print('Pode entrar')
else:
    print('Usuário não pode entrar')
