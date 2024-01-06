"""
Remover produto: 
    O usuário pode remover um produto da lista informando o nome do produto que deseja remover. 
    O programa atualiza automaticamente o valor total de todos os produtos.
"""


def removerProduto(listaProdutos):
    # produto a ser removido
    nomeRevomer_input = str(input('Nome do produto que deseja remover: '))

    listaProdutos_clone = listaProdutos[:]

    for produto in listaProdutos_clone:
    # produto = dicionário de cada item; contendo todas as informações de um produto
        
        if produto['nome'] == nomeRevomer_input:
            # localizando o produto
            print(f'Produto removido: {produto["nome"]}')

            listaProdutos.remove(produto)
            return listaProdutos # Retorna apenas se encontrar o produto a ser removido

    # caso o produto não exista
    print(f'Produto {nomeRevomer_input} não localizado')
    return listaProdutos # Retorna a lista original se o produto não for encontrado
