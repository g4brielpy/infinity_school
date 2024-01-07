'''
8)Considere a seguinte lista de palavras: [&quot;Python&quot;, &quot;é&quot;, &quot;uma&quot;, &quot;linguagem&quot;, &quot;poderosa&quot;].
Escreva um programa que itere sobre essa lista e exiba apenas as palavras que possuem mais de 4 letras.
'''

palavras = ['Python', 'é', 'uma', 'linguagem', 'poderosa']

print('Palavras que possuem mais de 4 letras')
for palavra in palavras:
    if len(palavra) > 4:
        print(palavra)