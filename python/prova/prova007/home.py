# módulos
import add_produtos
import del_produtos
import ver_produtos
import att_produtos

# variáveis
lista_produtos = list()

# Menu principal
while True:
    print('\nMENU DE PRODUTOS')
    print('-- '*6)

    print('[1] - Adicionar produtos')
    print('[2] - Remover produto')
    print('[3] - Lista de produtos')
    print('[4] - Atualizar produtos')
    print('[5] - Encerrar programa')
    comando = str(input('COMANDO: '))

    match comando:
        case '1':
            add_produtos.adicionarProduto(lista_produtos)
        case '2':
            del_produtos.removerProduto(lista_produtos)
        case '3':
            ver_produtos.exiberProduto(lista_produtos)
        case '4':
            att_produtos.atualizarProduto(lista_produtos)
        case '5':
            break
        case _:
            print('Valor inválido')
