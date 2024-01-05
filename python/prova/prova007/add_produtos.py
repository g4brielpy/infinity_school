"""
Adicionar produtos: 
    O usuário pode adicionar um novo produto à lista informando o NOME, a QUANTIDADE e o VALOR UNITÁRIO do produto. 
    O programa calcula automaticamente o VALOR TOTAL do produto (quantidade * valor unitário) e atualiza o valor total de todos os produtos.
"""


def adicionarProduto(listaProdutos):

    # cadastro do produto
    nome_input = str(input('Nome do produto: '))
    quantidade_input = int(input(f'Quantidade de {nome_input}: '))
    valorUnitario_input = float(input('Valor Unitário: R$ '))

    valorTotal = (quantidade_input * valorUnitario_input)

    produto = {
        'nome': nome_input,
        'quatidade': quantidade_input,
        'valor unitario': valorUnitario_input,
        'valor total': valorTotal
    }
    listaProdutos.append(produto)

    return listaProdutos
