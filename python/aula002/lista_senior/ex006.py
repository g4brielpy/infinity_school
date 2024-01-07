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

perguntas = ['Telefonou para a vítima ', 'Esteve no local do crime ', 'Mora perto da vítima ', 'Devia para a vítima ', 'Já trabalhou com a vítima ']
respostas = 0

for pergunta in perguntas:
    resposta = str(input(f'{pergunta} [S / N]: ').upper())
    if resposta == 'S':
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