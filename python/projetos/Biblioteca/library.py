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
    '''
    Iniciaizar a biblioteca com os atributos necessários
    '''

    def __init__(self, livros: list) -> None:
        self.catalogo_livros = livros
        self.registro_membros = []


livros = ['Código Limpo', 'Padrões de Projetos', 'Refatoração']
membros = ['Gabriel', 'Iuri']
biblioteca = Biblioteca(livros)


class Livro(Biblioteca):
    def __init__(self, titulo: str, autor: str, id_livro: int, status: str) -> None:
        self.titulo = titulo
        self.autor = autor
        self.id = id_livro
        self.status = status


class Membro:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.historico = []
