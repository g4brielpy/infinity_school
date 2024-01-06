"""
Ver a lista de produtos: 
    O programa exibe a lista de produtos adicionados até o momento, mostrando o nome do produto, o valor unitário, a quantidade e o valor total do produto. 
    Além disso, exibe o valor total de todos os produtos da lista.
"""


def exiberProduto(listaProdutos):

    for produto in listaProdutos:
        # produto = dicionário de cada item; contendo todas as informações de um produto
        print(f'PRODUTO {produto["nome"].upper()}')
        print(f'Nome: {produto["nome"]}')
        print(f'Quatidade: {produto["quantidade"]}')
        print(f'Valor unitário: R$ {produto["valor unitario"]}')
        print(f'TOTAL: R$ {produto["valor total"]}\n')
