'''
2)Dada a tupla de nomes de países: ('Brasil', 'Canadá', 'Austrália', 'Espanha', 'Índia'), 
crie um programa que itere sobre a tupla e exiba na tela cada país seguido pelo número de caracteres presentes em seu nome.
'''

paises = ('Brasil', 'Canadá', 'Austrália', 'Espanha', 'Índia')

for pais in paises:
    print(f'Pais: {pais}, tamanho: {len(pais)}')