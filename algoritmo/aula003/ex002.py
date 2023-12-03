respostas = 0

telefone = str(input('Telefonou para a vítima [s / n]: '))
local = str(input('Esteve no local do crime [s / n]: '))
moradia = str(input('Mora perto da vítima [s / n]: '))
divida = str(input('Devia para a vítima [s / n]: '))
trabalho = str(input('Já trabalhou com a vítima [s / n]: '))

if telefone == 's':
    respostas += 1

if local == 's':
    respostas += 1

if moradia == 's':
    respostas += 1

if divida == 's':
    respostas += 1

if trabalho == 's':
    respostas += 1

if respostas == 2:
    print('Suspeita')
elif respostas == 3 or respostas == 4:
    print('Cúmplice')
elif respostas == 5:
    print('Assassino')
else:
    print('Inocente')