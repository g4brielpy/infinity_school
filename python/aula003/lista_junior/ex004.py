# 4. crie uma variavel que retorne na tela todos os valores do dicionario da questão 2.

dados = {
    'nome': 'Gabriel',
    'sobrenome': 'Iuri',
    'idade': 18,
    'anivesario': '11/12'
}
valores = list()

for chave, valor in dados.items():
    valores.append(valor)
    
print(valores)