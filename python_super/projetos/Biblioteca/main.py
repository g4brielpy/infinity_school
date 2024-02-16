import library

MENU = '''
[] - Criar um Usuário
[] - Adicionar um Livro a Biblioteca
[] - Pegar um Livro Emprestado
[] - Devolver um Livro
[] - Pesquisar de Livro Por Título
=> '''

controle = True
while controle:
    opcao = str(input(MENU))

    match opcao:
        case '1':
            nome = str(input('Digite o nome: '))
            user = library.Membro(nome)
