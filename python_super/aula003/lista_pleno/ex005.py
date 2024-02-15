'''
Suponha que o dicionario da questão 1 seja um estoque de um sacolão e ele foi
renovado da seguinte forma:
    ● A Uva agora se chama “Uva sem semente”

Exiba o novo formato do dicionario na tela.
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
sacolao['Uva sem semente'] = sacolao['Uva']
sacolao.pop('Uva')

print(sacolao)