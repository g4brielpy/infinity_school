'''
Faça um programa em Python que, utilizando estruturas de repetição, calcule a média de idade dos alunos de uma turma. 
O programa deve pedir ao usuário a quantidade de alunos na turma e, em seguida, solicitar a idade de cada um. 
O programa deve utilizar um laço FOR para receber as idades dos alunos e um laço WHILE para realizar a soma das idades. 
Ao final, o programa deve exibir a média de idade da turma.
'''

idades = list()
quantidade_alunos = int(input('Qual a quantidade de alunos: '))

for i in range(1, quantidade_alunos + 1):
    idade = float(input(f'Digite {i}° idade: '))
    idades.append(idade)

media = sum(idades) / len(idades)

print(f'Média de idade dos alunos: {media}')