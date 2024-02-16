import library
from os import system

MENU = '''
[1] - Criar um Usuário
[2] - Adicionar um Livro a Biblioteca
[3] - Pegar um Livro Emprestado
[4] - Devolver um Livro
[] - Pesquisar de Livro Por Título
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
                print('ADICIONAR NOVO USUÁRIO\n')
                nome = str(input('Digite o nome: '))
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
                print('PEGAR LIVRO EMPRESTADO\n')
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
