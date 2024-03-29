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

'''
Imagine que você está desenvolvendo um sistema para gerenciar uma biblioteca. 

Nessa biblioteca, existem diferentes tipos de livros, como romances, biografias, livros infantis, etc. 

Todos esses livros possuem algumas características em comum, como o título, o autor e a editora, mas também possuem características específicas,

como o número de páginas, a faixa etária recomendada, etc.
'''




from random import randint
class Biblioteca:
    def __init__(self) -> None:
        '''
        Iniciaizar a biblioteca com os atributos necessários
        '''
        self.catalogo_livros: list = []

    def adicionarLivro(self, livro: dict) -> None:
        '''
        Adicionar um novo livro(class: Livro) ao catalogo de livros
        disponíveis da biblioteca.
        '''
        if livro:
            # Verifica se há um livro com os mesmos atributos no catálogo
            if not any(livro['titulo'] == l['titulo'] for l in self.catalogo_livros):
                self.catalogo_livros.append(livro)
            else:
                raise Exception('Livro já existe na biblioteca')
        else:
            raise Exception('Livro inválido')

    def listarLivros(self) -> str:
        '''
        Listar todos os livros disponíveis no catalogo da biblioteca
        '''
        catalogo: str = ''
        if self.catalogo_livros:
            for livro in self.catalogo_livros:
                catalogo += ', '.join([f'{chave.title()}: {valor}'
                                       for chave, valor in livro.items()]) + '\n'
            return catalogo
        else:
            return 'Não há livros para ser exibidos'

    def exibirDetalheLivro(self, titulo: str) -> str:
        '''
        Faz uma pesquisa no catalogo da biblioteca, utilizando o Título dos livros, 
        e retorna se foi encontrado um livro com o nome passado para a função ou não
        '''
        for livro in self.catalogo_livros:
            if livro['titulo'] == titulo:
                informacoes: str = ', '.join([f'{chave.title()}: {valor}'
                                              for chave, valor in livro.items()])
                return informacoes
        return 'Livro não encontrado!'

    def pesquisaLivroAutor(self, nome_autor: str) -> str:
        '''
        Faz uma pesquisa no catalogo da biblioteca, utilizando o Autor dos livros, 
        e retorna se foi encontrado um livro com o nome passado para a função ou não
        '''
        informacoes: str = ''
        for livro in self.catalogo_livros:
            if livro['autor'] == nome_autor:
                informacoes += ', '.join([f'{chave.title()}: {valor}'
                                          for chave, valor in livro.items()]) + '\n'
        if informacoes:
            return informacoes.rstrip()
        else:
            return 'Nenhum livro foi encontrado'

    def pesquisarLivroGenero(self, genero_livro: str) -> str:
        '''
        Faz uma pesquisa no catalogo da biblioteca, utilizando o Genero dos livros, 
        e retorna se foi encontrado um livro com o nome passado para a função ou não
        '''
        informacoes: str = ''
        for livro in self.catalogo_livros:
            if livro['genero'] == genero_livro.title():
                informacoes += ', '.join([f'{chave.title()}: {valor}'
                                          for chave, valor in livro.items()]) + '\n'
        if informacoes:
            return informacoes
        else:
            return 'Nenhum livro foi encontrado'


class Livro:
    def __init__(self, titulo: str, autor: str, qtd_pargina: int, tipo: str = 'Não informado') -> None:
        '''
        Iniciaizar um livro com os atributos necessários
        Adicionar a lista de livros da biblioteca
        '''
        self.titulo: str = titulo
        self.autor: str = autor
        self.paginas: int = qtd_pargina
        self.ID: str = self.gerarID()
        self.tipo: str = tipo

        '''Parâmetro para adicionar o livro à biblioteca'''
        self.livro = {
            'titulo': self.titulo,
            'autor': self.autor,
            'paginas': self.paginas,
            'genero': self.tipo,
            'id': self.ID,
            'status': 'disponivel',
        }
        biblioteca.adicionarLivro(self.livro)

    def gerarID(self) -> str:
        valores: list = [str(randint(0, 9)) for i in range(8)]
        id_livro: str = ''.join(valores)

        return id_livro


class Romance(Livro):
    def __init__(self, titulo: str, autor: str, qtd_pargina: int) -> None:
        self.tipo: str = 'Romance'
        super().__init__(titulo, autor, qtd_pargina, self.tipo)


class Biografia(Livro):
    def __init__(self, titulo: str, autor: str, qtd_pargina: int) -> None:
        self.tipo: str = 'Biografia'
        super().__init__(titulo, autor, qtd_pargina, self.tipo)


try:
    # I. Instânciando a Biblioteca para criar o sistema
    biblioteca = Biblioteca()

except Exception as e:
    print(f'ERRO ao criar uma biblioteca: {e}')
