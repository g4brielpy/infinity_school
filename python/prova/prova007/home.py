# módulos
import add_produtos
import del_produtos

# variáveis
lista_produtos = list()

# Menu principal
while True:
    print('\nMENU DE PRODUTOS')
    print('-- '*6)

    print('[1] - Adicionar produtos')
    print('[2] - Remover produto')
    print('[3] - Lista de produtos')
    print('[5] - Atualizar produtos')
    print('[6] - Encerrar programa')
    comando = str(input('COMANDO: '))

    match comando:
        case '1':
            add_produtos.adicionarProduto(lista_produtos)
        case '2':
            del_produtos.removerProduto(lista_produtos)
