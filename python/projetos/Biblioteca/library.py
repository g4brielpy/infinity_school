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
        
    def adicionarLivro(self, livro: object) -> None:
        '''
        Adicionar um novo livro(class) ao catalogo de livros
        disponíveis da biblioteca.
        '''
        if livro:
            self.catalogo_livros.append(livro)
        else:
            raise Exception('Livro inválido')
        


livros = ['Código Limpo', 'Padrões de Projetos', 'Refatoração']
membros = ['Gabriel', 'Iuri']
biblioteca = Biblioteca()


class Livro(Biblioteca):
    def __init__(self, titulo: str, autor: str, id_livro: int, status: str) -> None:
        '''
        Iniciaizar um livro com os atributos necessários
        '''
        self.titulo = titulo
        self.autor = autor
        self.ID = id_livro
        self.status = status


class Membro(Biblioteca):
    '''
    Iniciaizar um membro com os atributos necessários
    Adiciona a lista de membros da biblioteca
    '''
    def __init__(self, nome: str, id_user: int) -> None:
        self.nome = nome
        self.ID = id_user
        self.historico = []
        # super().registro_membros = 
