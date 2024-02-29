import library
from os import system


generos = [library.Romance, library.Biografia, library.Livro]
MENU = f'''
[1] - Adicionar Livro a Biblioteca
[2] - Pesquisar de Livro Por Título
[3] - Pesquisar de Livro Por Autor
[4] - Pesquisar de Livro Por Gênero
[5] - Ver Todos os Livros
[q] - Sair
=> '''

'''
Livros de exemplos:
    I.  codigo_limpo = Livro('Código Limpo', 'Robert C. Martin', 1)
    II. padroes_de_projetos = Livro('Padrões de Projetos', 'Erich Gamma', 1),
'''

controle = True
while controle:
    opcao = str(input(MENU))
    system('cls')

    match opcao:

        case '1':
            try:
                genero = int(
                    input('GÊNEROS\n [1] - Romance\n [2] - Biografica\n [3] - Outros\n => '))
                if genero not in [1, 2, 3]:
                    raise ValueError

                print('\nADICIONAR NOVO LIVRO\n')
                titulo = str(input('Título: '))
                autor = str(input('Autor ou Editora: '))
                qtd_paginas = int(input('Quantidade de páginas: '))
                novo_livro = generos[genero-1](titulo, autor, qtd_paginas)
            except ValueError:
                print('Opção inválida')
            except Exception as e:
                print('Erro ao criar o livro')
            else:
                print('Livro criado com sucesso!')

        case '2':
            try:
                print('PESQUISAR POR TÍTULO\n')
                titulo = str(input('Digite o Título do Livro: '))
                informacoes = library.biblioteca.exibirDetalheLivro(titulo)
            except:
                print('Erro ao pesquisar por livro')
            else:
                print(informacoes)

        case '3':
            try:
                print('PESQUISAR POR AUTOR\n')
                nome_autor = str(input('Digite o Nome do Autor: '))
                informacoes = library.biblioteca.pesquisaLivroAutor(nome_autor)
            except:
                print('Erro ao pesquisar por livros deste autor')
            else:
                print(informacoes)

        case '4':
            try:
                print('PESQUISAR POR GÊNERO\n')
                genero_livro = str(input('Digite o GÊNERO do Livro: '))
                informacoes = library.biblioteca.pesquisarLivroGenero(
                    genero_livro)
            except:
                print('Erro ao pesquisar por livro')
            else:
                print(informacoes)

        case '5':
            try:
                catalogo = library.biblioteca.listarLivros()
            except:
                print('Erro ao listar livros')
            else:
                print('LIVROS DISPONÍVEIS\n')
                print(catalogo)

        case 'q':
            controle = False
            print('Biblioteca Encerrada!\n')

        case _:
            print('Opção inválida!')
