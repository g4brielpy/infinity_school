'''
Com o dicionário da questão 1, mostre ao usuário a lista de chaves e pergunte se
ele quer eliminar algum item. Caso a resposta seja 'SIM', solicite o item que deseja
deletar e elimine-o do dicionário.
'''

sacolao = {
    'Maçã': 3,
    'Banana': 6,
    'Laranja': 4,
    'Pêra': 5,
    'Uva': 2,
    'Abacaxi': 1,
    'Melancia': 7,
    'Morango': 8
}

deseja_eliminar = str(
    input('Deseja eliminar alguma chave [SIM / NAO]: ').upper())

if deseja_eliminar == 'SIM':
    chave_del = str(input('Qual chave que deseja remover: '))
    sacolao_del = sacolao.pop(chave_del, 'Não encontrou')

if sacolao_del == 'Não encontrou':
    print(sacolao_del)
else:
    print('Chave removida')
