# Altere o valor da chave nome do dicionario da questão 2.

dados = {
    'nome': 'Gabriel',
    'sobrenome': 'Iuri',
    'idade': 18,
    'anivesario': '11/12'
}
dados['nome1'] = dados['nome']
dados.pop('nome')

print(dados)
