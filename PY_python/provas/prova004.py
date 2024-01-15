'''
[PY-A04]Escreva uma função em Python que recebe dois números como argumentos e retorna o maior entre eles.

a) Implemente a função com o nome "maior_numero" e utilizando condicionais.
b) Implemente a mesma função, porém utilizando a função "max".
'''

numb1 = float(input('Digite um número: '))
numb2 = float(input('Digite outro número: '))


def maior_numero(x, y):
    if x > y:
        return f'a) {x} é maior que {y}'
    elif x == y:
        return f'a) Os valores são iguais'
    else:
        return f'a) {y} é maior que {x}'

numero = maior_numero(numb1, numb2)
print(numero)

maior_numero_max = max(numb1, numb2)
print(f'b) maior número é {maior_numero_max}')