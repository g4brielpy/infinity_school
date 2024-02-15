'''
Suponha que o dicionario da questão 1 seja um estoque de um sacolão e ele foi
renovado da seguinte forma:
    ● chegaram 45 Maçãs
    ● venderam 3 Morangos
    ● chegaram 27 Uvas
Exiba este novo dicionario na tela.
'''

sacolao = {
    'Maçã': 3,
    'Banana': 6,
    'Laranja': 4,
    'Pêra': 5,
    'Uva': 2,
    'Abacaxi': 1,
    'Melancia': 7,
    'Morango': 8
}

sacolao['Maçã'] += 45
sacolao['Morango'] += 3
sacolao['Uva'] += 27

print(sacolao)
