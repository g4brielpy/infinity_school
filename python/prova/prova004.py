'''
Desenvolva um programa em Python que permita ao usuário digitar várias notas. 

Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno.

Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: 

"Reprovado" se a média for menor que 7, 
"Aprovado" se a média for maior ou igual a 7, e
"Parabéns, sua média é 10" se a média for igual a 10.
'''
# variáveis
lista_notas = list()
media = float()
quantidad_notas = 1

# funções
def calcular_media(notas_aluno):
    media_aluno = sum(notas_aluno) / len(notas_aluno)
    return media_aluno

# coletar notas
while True:

    notas = str(input(f'\nDigite sua {quantidad_notas}° Nota: '))
    # verificar se a nota é valida e atribuir o valor da lista
    if notas.isdigit():
        notas = int(notas)

        lista_notas.append(notas)
        quantidad_notas += 1

    else:
        print('Valor inválido! Informe novamente')
        continue

    while True:
    # verificar se o user vai informar outra nota
        mais_notas = str(input('\nDeseja informar outra Nota [S / N]: ').upper())
        if (mais_notas == 'S') or (mais_notas == 'N'):
            break

        else:
            print('valor inválido!')
    if (mais_notas == 'S'):
        continue
    else:
        break

# chamada da função média
media = calcular_media(lista_notas)
print(f'A média do aluno é: {media}')
    