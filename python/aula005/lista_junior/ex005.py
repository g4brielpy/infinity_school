'''
5)Concatenação de strings:
Escreva uma função chamada concatena_strings que aceita um número variável de 
argumentos do tipo string e retorna uma única string contendo a concatenação de todas elas

valor_par = lambda x: x % 2 == 0
print(valor_par(4))
'''

concatena_strings = lambda *x: ' '.join(x)
print(concatena_strings('a', 'b', 'c'))
