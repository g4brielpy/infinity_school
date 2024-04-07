class Endereco:
    def __init__(self, lougradouro: str, bairro: str, cidade: str, estado: str, numero: int, complemento: str = "") -> None:
        self.__lougradouro = lougradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.numero = numero
        self.complemento = complemento

    # configura como o endereço do objeto vai ser exibido no terminal
    def __repr__(self) -> str:
        return f"<Class Endereco - {self.__lougradouro} / {self.numero}>"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Endereco):
            return False

        return (
            self.cidade == value.cidade and
            self.bairro == value.bairro and
            self.numero == value.numero and
            self.complemento == value.complemento
        )


endereco = Endereco("Rua Nossa Senhora", "Barreiro",
                    "Belo Horizonte", "Minas Gerais", 190)
