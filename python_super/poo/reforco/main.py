class Pessoa:
    total_pessoas = 0
    total_estudante = 0

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas += 1

    def apresentar(self) -> str:
        return f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.'


class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, ano_letivo: str) -> None:
        super().__init__(nome, idade)
        self.ano_letivo = ano_letivo
        Pessoa.total_estudante += 1
