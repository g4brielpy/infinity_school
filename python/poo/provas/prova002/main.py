'''
Crie um código em Python que contenha as seguintes classes:

A classe principal será chamada de "Material" e terá um construtor que recebe dois parâmetros: "titulo" e "autor_ou_editora". Essa classe também terá um método chamado "exibir_informacoes" que imprimirá na saída o título e o autor/editora do material.

A classe "Livro" será uma subclasse da classe "Material" e terá um construtor que recebe três parâmetros: "titulo", "autor_ou_editora" e "genero". Essa classe também terá um método "exibir_informacoes" que chamará o método correspondente na classe "Material" e imprimirá o gênero do livro.

A classe "Revista" será outra subclasse da classe "Material" e terá um construtor que recebe três parâmetros: "titulo", "autor_ou_editora" e "edicao". Essa classe também terá um método "exibir_informacoes" que chamará o método correspondente na classe "Material" e imprimirá a edição da revista.

Crie instâncias das classes "Livro" e "Revista" com informações específicas e chame o método "exibir_informacoes" para mostrar os detalhes de cada material.
'''


class Material:
    def __init__(self, titulo: str, autor_editora: str) -> None:
        self.titulo = titulo
        self.autor_editora = autor_editora

    def exibir_informacoes(self) -> str:
        return f'Título: {self.titulo} \nAutor/Editora: {self.autor_editora}'


class Livro(Material):
    def __init__(self, titulo: str, autor_editora: str, genero: str) -> None:
        super().__init__(titulo, autor_editora)
        self.genero = genero

    def exibir_informacoes(self) -> str:
        return f'{super().exibir_informacoes()} \nGenero: {self.genero}'


class Revista(Material):
    def __init__(self, titulo: str, autor_editora: str, edicao: str) -> None:
        super().__init__(titulo, autor_editora)
        self.edicao = edicao

    def exibir_informacoes(self):
        return f'{super().exibir_informacoes()} \nEdição: {self.edicao}'


print('\nInstâncias das classes "Livro"')
livro = Livro('Entendendo Algoritmos', 'Aditya Y. Bhargava', 'Tecnologia')
print(livro.exibir_informacoes())

print('\nInstâncias das classes "Revista"')
revista = Revista('Java Magazine', 'DevMedia', '156')
print(revista.exibir_informacoes())
