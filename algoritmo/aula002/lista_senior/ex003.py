print('\nDetetive!\n')

# perguntas
perg1 = str(input('Telefonou para a vítima? [s/n] '.lower()))
perg2 = str(input('Esteve no local do crime? [s/n] '.lower()))
perg3 = str(input('Mora perto da vítima? [s/n] '.lower()))
perg4 = str(input('Devia para a vítima? [s/n] '.lower()))
perg5 = str(input('Já trabalhou com a vítima? [s/n] '.lower()))
resposta = 0

if (perg1 == 's'):
    resposta += 1

if (perg2 == 's'):
    resposta += 1

if (perg3 == 's'):
    resposta += 1

if (perg4 == 's'):
    resposta += 1

if (perg5 == 's'):
    resposta += 1

# verificar a quantidade de 'sim'
if (resposta == 2):
    print('Suspeita')
elif(resposta == 3) or (resposta == 4):
    print('Cúmplice')
elif (resposta == 5):
    print('Assassino')
else:
    print('Inocente')