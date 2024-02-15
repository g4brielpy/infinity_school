# crie uma lista de tuplas com o dicionario da questao dois exibindo a chave e o valor.

dados = {
    'nome': 'Gabriel',
    'sobrenome': 'Iuri',
    'idade': 18,
    'anivesario': '11/12'
}

chaves_dados = list()
valores_dados = list()

for chave, valor in dados.items():
    chaves_dados.append(chave)
    valores_dados.append(valor)

chaves_dados = tuple(chaves_dados)
valores_dados = tuple(valores_dados)
lista_valores = list([chaves_dados, valores_dados])

print(chaves_dados)
print(valores_dados)
print(lista_valores)
