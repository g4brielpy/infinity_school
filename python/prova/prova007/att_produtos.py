"""
Atualizar produtos: 
    O usuário pode atualizar as informações de um produto existente na lista. 
    O programa solicita o nome do produto que deseja atualizar e, em seguida, permite editar o nome, a quantidade e o valor unitário do produto. O programa recalcula automaticamente o valor total do produto e o valor total de todos os produtos.
"""
def atualizarProduto(listaProdutos):
    nomeAtualizar_input = str(input('Nome do produto que deseja atualizar: '))

    for produto in listaProdutos:
    # produto = dicionário de cada item; contendo todas as informações de um produto
        
        if produto['nome'] == nomeAtualizar_input:
            # localizando o produto

            # alterar nome
            while True:
                x = str(input('Deseja alterar o nome [S / N]: ').upper())
                if x == 'S':
                    novo_nome = str(input('Novo nome: '))
                    produto['nome'] = novo_nome
                    break
                else:
                    break

            # alterar quantidade
            while True:
                x = str(input('Deseja alterar a quantidade [S / N]: ').upper())
                if x == 'S':
                    nova_quantidade = int(input('Nova quantidade: '))
                    produto['quantidade'] = nova_quantidade
                    break
                else:
                    break

            # alterar valor unitário
            while True:
                x = str(input('Deseja alterar o valor unitário [S / N]: ').upper())
                if x == 'S':
                    novo_valor = float(input('Novo valor: '))
                    produto['valor unitario'] = novo_valor
                    break
                else:
                    break

            return listaProdutos


    print(f'Produto {nomeAtualizar_input} não localizado')
    return listaProdutos # Retorna a lista original se o produto não for encontrado
