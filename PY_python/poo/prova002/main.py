'''
Desenvolva um exemplo de aplicação de polimorfismo utilizando super classe.

Crie uma classe pai que defina um método genérico, e em seguida crie duas ou mais classes filhas que herdem essa super classe

e sobrescrevam o método de acordo com suas necessidades.
'''


class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def fazer_som(self) -> None:
        pass


class Cachorro(Animal):
    def __init__(self, nome: str, raca: str) -> None:
        super().__init__(nome)
        self.raca = raca

    def fazer_som(self) -> str:
        return "Au au!"


class Gato(Animal):
    def __init__(self, nome: str, raca: str) -> None:
        super().__init__(nome)
        self.raca = raca

    def fazer_som(self) -> str:
        return "Miau!"



cachorro = Cachorro('Bob', 'Pinscher')
gato = Gato('Rob', 'Persa')

print(cachorro.nome)
print(cachorro.fazer_som())

print(gato.nome)
print(gato.fazer_som())
