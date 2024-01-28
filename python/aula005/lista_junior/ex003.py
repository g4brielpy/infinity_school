'''
3)Média de todos os argumentos:
Escreva uma função chamada media_args que aceita um número variável de argumentos e retorna a média de todos eles
'''

def media_args(*args):
    args = list(args)
    media = sum(args) / len(args)
    return media

valores = (1, 5, 8 ,10)
print(f'A media dos valores {valores} é: {media_args(*valores)}')
