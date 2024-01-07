'''
6)Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um
crime. As perguntas são:
&quot;Telefonou para a vítima?&quot;
&quot;Esteve no local do crime?&quot;
&quot;Mora perto da vítima?&quot;
&quot;Devia para a vítima?&quot;
&quot;Já trabalhou com a vítima?&quot; O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
deve ser classificada como &quot;Suspeita&quot;, entre 3 e 4 como &quot;Cúmplice&quot; e 5 como &quot;Assassino&quot;.
Caso contrário, ele será classificado como &quot;Inocente&quot;.
'''

respostas = 0

pergunta1 = str(input('Telefonou para a vítima? [S / N] ').upper())
if pergunta1 == 'S':
    respostas += 1

pergunta2 = str(input('Esteve no local do crime? [S / N] ').upper())
if pergunta2 == 'S':
    respostas += 1

pergunta3 = str(input('Mora perto da vítima? [S / N] ').upper())
if pergunta3 == 'S':
    respostas += 1

pergunta4 = str(input('Devia para a vítima? [S / N] ').upper())
if pergunta4 == 'S':
    respostas += 1

pergunta5 = str(input('Já trabalhou com a vítima? [S / N] ').upper())
if pergunta5 == 'S':
    respostas += 1


if respostas <= 1:
    print('Inocente')
elif respostas == 2:
    print('Suspeita')
elif respostas in (3, 4):
    print('Cúmplice')
elif respostas == 5:
    print('Assasino')
else:
    print('Valor inválido')