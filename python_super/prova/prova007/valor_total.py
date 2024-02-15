"""
Valor total de todos os produtos
"""


def valorTotal(listaProdutos):
    produtos_precos = list()

    # lista com todos os preços
    for produto in listaProdutos:
        produtos_precos.append(produto['valor total'])

    total = sum(produtos_precos)
    return total
