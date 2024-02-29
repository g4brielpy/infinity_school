import library
from os import system

MENU = f'''
[1] - Adicionar Livro a Biblioteca
[2] - Pegar Livro Emprestado
[3] - Devolver um Livro
[4] - Pesquisar de Livro Por Título
[5] - Pesquisar de Livro Por Autor
[6] - Pesquisar de Livro Por Gênero
[7] - Ver Todos os Livros
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
                print('ADICIONAR NOVO LIVRO\n')
                titulo = str(input('Título: '))
                autor = str(input('Autor ou Editora: '))
                qtd_paginas = int(input('Quantidade de páginas: '))
                novo_livro = library.Livro(titulo, autor, qtd_paginas)
            except:
                print('Erro ao criar o livro')
            else:
                print('Livro criado com sucesso!')

        case '2':
            try:
                catalogo = library.biblioteca.listarLivros()
                print('PEGAR LIVRO EMPRESTADO')
                print(f'Livros Disponíveis: \n{catalogo}')
                livro_emprestimo = str(input('Título do livro: '))
                library.biblioteca.emprestimoLivro(livro_emprestimo)
            except:
                print('Erro ao pegar o livro emprestado')
            else:
                print('Livro emprestado com sucesso!')

        case '3':
            try:
                print('DEVOLVER LIVRO\n')
                livro_devolver = str(input('Título do livro: '))
                library.biblioteca.devolucaoLivro(livro_devolver)
            except:
                print('Erro ao tentar devolver o livro')
            else:
                print('Livro devolvido com sucesso!')

        case '4':
            try:
                print('PESQUISAR POR TÍTULO\n')
                titulo = str(input('Digite o Título do Livro: '))
                informacoes = library.biblioteca.pesquisaLivroTitulo(titulo)
            except:
                print('Erro ao pesquisar por livro')
            else:
                print(informacoes)

        case '5':
            try:
                print('PESQUISAR POR AUTOR\n')
                nome_autor = str(input('Digite o Nome do Autor: '))
                informacoes = library.biblioteca.pesquisaLivroAutor(nome_autor)
            except:
                print('Erro ao pesquisar por livros deste autor')
            else:
                print(informacoes)

        case '6':
            try:
                print('PESQUISAR POR GÊNERO\n')
                genero_livro = str(input('Digite o GÊNERO do Livro: '))
                informacoes = library.biblioteca.pesquisarLivroGenero(
                    genero_livro)
            except:
                print('Erro ao pesquisar por livro')
            else:
                print(informacoes)

        case '7':
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
