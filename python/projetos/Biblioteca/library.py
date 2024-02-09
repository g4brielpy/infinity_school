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
        Adicionar um novo livro(class: Livro) ao catalogo de livros
        disponíveis da biblioteca.
        '''
        if livro:
            # Verifica se há um livro com os mesmos atributos no catálogo
            if not any(livro['titulo'] == l['titulo'] and livro['autor'] == l['autor']
                       and livro['id'] == l['id'] for l in self.catalogo_livros):
                self.catalogo_livros.append(livro)
            else:
                raise Exception('Livro já existe na biblioteca')
        else:
            raise Exception('Livro inválido')

    def adicionarMembro(self, membro: dict):
        '''
        Adicionar um novo membro(class: Membro) ao registro de membros
        cadastrados na biblioteca
        '''
        if membro:
            # Verifica se há um membro com o mesmo ID no registro
            if not any(membro['id'] == m['id'] for m in self.registro_membros):
                self.registro_membros.append(membro)
            else:
                raise Exception('Membro já existe na biblioteca')
        else:
            raise Exception('Membro inválido')


class Livro:
    def __init__(self, titulo: str, autor: str, id_livro: int) -> None:
        '''
        Iniciaizar um livro com os atributos necessários
        Adicionar a lista de livros da biblioteca
        '''
        self.titulo = titulo
        self.autor = autor
        self.ID = id_livro
        self.status = 'disponivel'
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


try:
    biblioteca = Biblioteca()

    codigo_limpo = Livro('Código Limpo', 'Robert C. Martin', 1)
    codigo_limpo2 = Livro('Código Limpo', 'Robert C. Martin', 1)
    padroes_de_projetos = Livro('Padrões de Projetos', 'Erich Gamma', 2)

    biblioteca.adicionarLivro(codigo_limpo.livro)
    biblioteca.adicionarLivro(codigo_limpo2.livro)
    gabriel = Membro('Gabriel', 123)
    
except Exception as e:
    print(e)

print(biblioteca.catalogo_livros)