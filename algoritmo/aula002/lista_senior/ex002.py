# preço dos combustíveis
alcool = 1.90
gasolina = 2.50

# tipo do combustíveis
combustivel = str(input('\nQual o tipo de Combustível: (A - Álcool) (G - Gasolina) ').upper())
litros = float(input('Digite a quantidade de litros: '))

# calcular o desconto
if (combustivel == 'A'):
    combustivel = alcool
    if (litros <= 20):
        desconto = 3/100
    else:
        desconto = 5/100
    valor_desconto = (combustivel - desconto) * litros

elif (combustivel == 'G'):
    combustivel = gasolina
    if (litros <= 20):
        desconto = 4/100
    else:
        desconto = 6/100
    valor_desconto = (combustivel - desconto) * litros

else:
    print('Valor inválido!')

print(valor_desconto)