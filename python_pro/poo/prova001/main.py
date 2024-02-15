'''
Crie uma classe utilizando os conceitos de POO das aulas passadas.

Para criar sua classe, pense em uma entidade do mundo real que possa ser representada de maneira simples e objetiva. 

Por exemplo, uma classe "Pessoa" poderia ter atributos como nome, idade e endereço, e métodos como cumprimentar e se movimentar.

Já uma classe "Animal" poderia ter atributos como espécie, peso e altura, e métodos como andar e dormir.
'''


class Pessoa:
    def __init__(self, nome: str, idade: int, endereco: str) -> None:
        # atributos
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def apresentar(self) -> str:
        return f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.'
    
    def dormir(self) -> str:
        return 'Estou indo dormir!'


class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, endereco: str, ano: int) -> None:
        super().__init__(nome, idade, endereco)

        if self.idade >= 15 and ano <= 3:
            self.ano_escolar = f'{ano}° Ensino médio'
        else:
            self.ano_escolar = f'{ano}° Ensino Fundamental'

    def apresentar(self) -> str:
        return f'Olá, meu nome é {self.nome} e tenho {self.idade} anos. Estou no {self.ano_escolar}'
    
    def estudar(self) -> str:
        return f'Estou estudando!'
