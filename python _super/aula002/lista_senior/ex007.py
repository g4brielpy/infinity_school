'''
7)Você recebeu uma lista de tuplas, onde cada tupla contém o nome de um produto e seu preço. 
Por exemplo: [(&quot;Maçã&quot;, 2.50), (&quot;Banana&quot;, 1.75), (&quot;Laranja&quot;, 3.00)]. 
Escreva um programa que itere sobre essa lista e calcule o valor total dos produtos, exibindo-os na tela.
'''

produtos = [('Maçã', 2.50), ('Banana', 1.75), ('Laranja', 3.00)]
valor_total = 0

for produto in produtos:
    for valor in produto:
        if type(valor) == float:
            print(valor)
            valor_total += valor

print(f'Valor total de todos os produtos: {valor_total}')