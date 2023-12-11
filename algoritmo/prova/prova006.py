'''
Escreva um código em Python que peça três números e determine:
- O maior número;
- O menor número;
- Se existem números iguais e caso exista, quais são os números.
'''
valores = [ ]
for i in range(1, 4):
    x = int(input(f'Digite o {i}° valor: '))
    valores.append(x)

print(valores)