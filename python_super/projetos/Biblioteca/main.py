import library
from os import system

MENU = f'''
MEMBRO: {library.user.nome}
[1] - Criar um Usuário
[2] - Adicionar Livro a Biblioteca
[3] - Pegar Livro Emprestado
[4] - Devolver um Livro
[5] - Pesquisar de Livro Por Título
[6] - Pesquisar de Livro Por Autor
[7] - Pesquisar de Livro Por &
[q] - Sair
=> '''

'''
Livros de exemplos:
    I.  codigo_limpo = Livro('Código Limpo', 'Robert C. Martin', 1)
    II. padroes_de_projetos = Livro('Padrões de Projetos', 'Erich Gamma', 2),
'''

controle = True
while controle:
    opcao = str(input(MENU))
    system('cls')

    match opcao:
        case '1':
            try:
                # ARRUMAR MÉTODO DE USUÁRIO
                print('ADICIONAR NOVO USUÁRIO\n')
                nome = str(input('Digite o nome: ').strip)
                library.user.definirNome(nome)
            except:
                print('Erro ao criar o usuário!')
            else:
                print('Usuário criado com sucesso!')

        case '2':
            try:
                print('ADICIONAR NOVO LIVRO\n')
                titulo = str(input('Título: '))
                autor = str(input('Autor ou Editora: '))
                novo_livro = library.Livro(titulo, autor)
            except:
                print('Erro ao criar o livro')
            else:
                print('Livro criado com sucesso!')

        case '3':
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

        case '4':
            try:
                print('DEVOLVER LIVRO\n')
                livro_devolver = str(input('Título do livro: '))
                library.biblioteca.devolucaoLivro(livro_devolver)
            except:
                print('Erro ao tentar devolver o livro')
            else:
                print('Livro devolvido com sucesso!')

        case '5':
            try:
                print('PESQUISAR POR TÍTULO\n')
                titulo = str(input('Digite o Título do Livro: '))
                informacoes = library.biblioteca.pesquisaLivroTitulo(titulo)
            except:
                print('Erro ao pesquisar por livro')
            else:
                print(informacoes)

        case '6':
            try:
                print('PESQUISAR POR AUTOR\n')
                nome_autor = str(input('Digite o Nome do Autor: '))
                informacoes = library.biblioteca.pesquisaLivroAutor(nome_autor)
            except:
                print('Erro ao pesquisar por livros deste autor')
            else:
                print(informacoes)

        case 'q':
            controle = False
            print('Biblioteca Encerrada!\n')

        case _:
            print('Opção inválida!')
