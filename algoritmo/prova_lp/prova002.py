'''
Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.
'''
km_max = 80.00
multa = float

velocidade_carro = float(input('Qual a velocidade(Km/h) que o carro estava: '))
if velocidade_carro > km_max:
    multa = (velocidade_carro - km_max) * 20
    print(f'Você tomou uma multa no valor de R$ {multa:,.2f}')
else:
    print('Parabens! Você não foi multado.')
