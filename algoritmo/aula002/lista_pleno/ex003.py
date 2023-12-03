nota_1 = float(input('Digite a 1° nota: '))
nota_2 = float(input('Digite a 2° nota: '))
media = float((nota_1 + nota_2) / 2)

if (media >= 7) and (media < 10):
    print('Você foi aprovado, Parabéns!')
elif (media < 7) and (media >= 0):
    print('Reprovado!')
elif (media == 10):
    print('Aprovado com Distinção, Parabens!')
else:
    print('Nota invalida!')