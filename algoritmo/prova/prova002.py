# velocidade de um carro
km_max = 80.00
multa = float

velocidade_carro = float(input('Qual a velocidade(Km/h) que o carro estava: '))

if (velocidade_carro > km_max):
    multa = (velocidade_carro - km_max)
    print('Você foi multado!')
    print(f'O valor da multa é R$ {round(multa, 3)}')
else :
    print('Parabens! Você não foi multado.')