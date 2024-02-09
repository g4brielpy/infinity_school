'''
Criar uma aplicação de gerenciamento de biblioteca com

Classe Livro:
    A classe Livro deve conter atributos como título, autor, ID,
    estatus de empréstimo (disponível ou emprestado).

Classe Membro:
    A classe Membro deve conter atributos como nome,
    número de membro e histórico de livros emprestados.

Classe Biblioteca:
    A classe Biblioteca deve conter um catálogo de livros
    disponíveis, um registro de membros e métodos para
    empréstimo, devolução e pesquisa de livros.
'''


class Biblioteca:
    def __init__(self) -> None:
        '''
        Iniciaizar a biblioteca com os atributos necessários
        catalogo e membros vazio
        '''
        self.catalogo_livros = []
        self.registro_membros = []

    def adicionarLivro(self, livro: dict) -> None:
        '''
        Adicionar um novo livro(class) ao catalogo de livros
        disponíveis da biblioteca.
        '''
        if livro:
            self.catalogo_livros.append(livro)
        else:
            raise Exception('Livro inválido')


class Livro:
    def __init__(self, titulo: str, autor: str, id_livro: int, status: str) -> None:
        '''
        Iniciaizar um livro com os atributos necessários
        Adicionar a lista de livros da biblioteca
        '''
        self.titulo = titulo
        self.autor = autor
        self.ID = id_livro
        self.status = status
        '''Parâmetro para adicionar o livro à biblioteca'''
        self.livro = {
            'titulo': self.titulo,
            'autor': self.autor,
            'id': self.ID,
            'status': self.status
        }


class Membro:
    def __init__(self, nome: str, id_user: int) -> None:
        '''
        Iniciaizar um membro com os atributos necessários
        Adiciona a lista de membros da biblioteca
        '''
        self.nome = nome
        self.ID = id_user
        self.historico = []
        '''Parâmetro para adicionar o membro à biblioteca'''
        self.dados = {
            'nome': self.nome,
            'id': self.ID,
            'histórico de livros': self.historico
        }


codigo_limpo = Livro('Código Limpo', 'Robert C. Martin', 1, 'Disponível')
padroes_de_projetos = Livro('Padrões de Projetos',
                            'Erich Gamma', 2, 'Emprestado')

gabriel = Membro('Gabriel', 123)

biblioteca = Biblioteca()
