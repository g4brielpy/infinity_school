'''
4)Faça um Programa que leia 4 notas, mostre as notas e a média na tela. utilizar listas
'''

notas = []
for i in range(0, 4):
    nota = float(input('Digite o valor da nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f'Notas do aluno: {notas}')
print(f'Media: {media}')