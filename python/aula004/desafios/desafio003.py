'''
Exercício 3: Gerador de Senhas

Aluno 1: Desenvolva uma função que gera senhas aleatórias com base em critérios definidos, como cumprimento e caracteres permitidos.
Aluno 2: Crie um menu para permitir ao usuário gerar senhas personalizadas.
'''

from random import choice
import string


def gera_senha_padrao():
    '''
    Senha Padrão de 9 caracteres:
        . Contem todos as letras minúsculas
        . Contem todos as letras maiúsculas
        . Contem todos os números
        . Contem todos os caracteres de pontuação
    '''
    caracteres = string.ascii_letters + string.digits + string.punctuation
    tamanho = 9

    senha = ''.join(choice(caracteres) for _ in range(tamanho))
    return senha


def gera_senha_personalizada(escolhas, tamanho):
    caracteres = ''
    caracteres_disponiveis = [string.ascii_lowercase,
                              string.ascii_uppercase, string.punctuation]

    for index, escolha in enumerate(escolhas):
        if escolha == 'S':
            caracteres += caracteres_disponiveis[index]

    senha = ''.join(choice(caracteres) for _ in range(tamanho))
    return senha


MENU = '''
GERADOR DE SENHA
[1] - Senha Padrão
[2] - Senha Personalizada
[q] - Sair
=> '''

while True:
    comando = input(MENU)

    match comando:
        case '1':
            senha = gera_senha_padrao()
            print(f'Sua senha é: {senha}')

        case '2':
            escolhas = []
            tamanho = int(input('Quantidade de caracteres: '))
            opcoes_caracteres = ['Letras minúsculas',
                                 'Letras maiúsculas', 'Caracteres especiais']

            for i in opcoes_caracteres:
                opcao = input(f'{i} [S/N]: ').upper()
                escolhas.append(opcao)

            senha = gera_senha_personalizada(escolhas, tamanho)
            print(f'Sua senha é: {senha}')

        case 'q':
            print('Programa finalizado')
            break

        case _:
            print('Valor inválido!')
