from textos.caracter import alfabeto
from textos.morse import alfabeto_mos

posicoes = list([6, 0, 1, 17, 8, 4, 11])

nome = str()
for posicao in posicoes:
    nome += ''.join(alfabeto(posicao))

nome_mos = alfabeto_mos('Gabriel')
print(nome_mos)
