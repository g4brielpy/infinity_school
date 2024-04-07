from datetime import datetime
from endereco import Endereco


class Pessoa:
    def __init__(self, nome: str, data_nascimento: str) -> None:
        self.nome = nome
        self.data_nascimento = datetime.strptime(
            data_nascimento, "%d/%m/%Y").date()

    def calcular_idade(self):
        data_atual = datetime.now().date()
        idade = data_atual - self.data_nascimento
        return idade.days // 365

    def __repr__(self) -> str:
        return f"<Class Pessoa - Nome: {self.nome}>"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Pessoa):
            return False

        return (
            self.nome == value.nome and
            self.data_nascimento == value.data_nascimento
        )

    def desconto(self):
        pass


class PessoaFisica(Pessoa):
    def __init__(self, nome: str, data_nascimento: str, cpf: str) -> None:
        super().__init__(nome, data_nascimento)
        self.cpf = cpf

    def desconto(self) -> float:
        return 0.03


class PessoaJuridica(Pessoa):
    def __init__(self, nome: str, data_nascimento: str, cnpj: str) -> None:
        super().__init__(nome, data_nascimento)
        self.cnpj = cnpj

    def desconto(self) -> float:
        return 0.05


pessoa = PessoaFisica("Gabriel", "07/04/2023", "000")
