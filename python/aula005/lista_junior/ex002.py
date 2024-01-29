'''
2)Produto de todos os argumentos:
Escreva uma função chamada produto_args que aceita um número variável de argumentos e retorna o produto de todos eles.
'''

def produto_args(lista_numeros):
    produto = 1
    for numero in lista_numeros:
        produto *= numero
    return produto



lista_numeros = []
while True:
    numero = input('Digite um número, se quiser para aperte "N": ').upper()
    if numero == 'N':
        break
    else:
        numero = int(numero)
    lista_numeros.append(numero)

    

resultado = produto_args(lista_numeros)
print(f'\nO produtos do valores digitados é: {resultado}')
        
