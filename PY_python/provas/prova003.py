'''
[PY-A03]Considere o seguinte dicionário em Python:

pessoas = {
    "João": 23,
    "Maria": 28,
    "Pedro": 35,
    "Lucas": 19
}

a) Acesse a idade da pessoa "João" e armazene em uma variável chamada idade_joao.
b) Adicione uma nova pessoa ao dicionário com nome "Ana" e idade 31.
c) Crie uma função chamada maior_idade que recebe um dicionário como argumento e retorna o nome da pessoa com a maior idade.
'''

pessoas = {
    "João": 23,
    "Maria": 28,
    "Pedro": 35,
    "Lucas": 19
}

idade_joao = pessoas["João"]
pessoas.update({'Ana': 31})


def maior_idade(dicionario_pessoas):
    idade = 0

    for chave, valor in dicionario_pessoas.items():
        if valor > idade:
            pessoa_mais_velha = chave
            idade = valor

    return pessoa_mais_velha


pessoa_mior_idade = maior_idade(pessoas)
print(f'A pessoa mais velha é {pessoa_mior_idade} com {
      pessoas[pessoa_mior_idade]} anos')
