# variáveis
lista_notas = list()
media = float()
situacao = str()
quantidad_notas = 1

# funções


def calcular_media(notas_aluno):
    media_aluno = sum(notas_aluno) / len(notas_aluno)
    return media_aluno


def verificar_situacao(media):
    if (media == 10):
        return ('Parabéns, sua média é 10')
    elif (media >= 7) and (media < 10):
        return ('Aprovado')
    else:
        return ('Reprovado')


# coletar notas
while True:

    notas = str(input(f'\nDigite sua {quantidad_notas}° Nota: '))
    # verificar se a nota é valida e atribuir o valor da lista
    if notas.isdigit():
        notas = int(notas)

        if (notas > 10) or (notas < 0):
            print('Valor inválido! Digite sua nota entre 0 a 10.')
            continue

        lista_notas.append(notas)
        quantidad_notas += 1

    else:
        print('Valor inválido! Informe novamente')
        continue

    while True:
        # verificar se o user vai informar outra nota
        mais_notas = str(
            input('\nDeseja informar outra Nota [S / N]: ').upper())
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
situacao = verificar_situacao(media)

print(f'\nA média do aluno é: {media}')
print(f'Situação do aluno: {situacao}')
