class Celular:
    def __init__(self, marca: str, modelo: str, cor: str) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.status = False

    def exibirInfo(self) -> None:
        print(
            f"Marca: {self.marca}, Modelo: {self.modelo} \nCor: {self.cor}, Status: {self.status}"
        )

    def ligar(self) -> None:
        self.status = True

    def desligar(self) -> None:
        self.status = False


meu_celular = Celular(
    marca="Xiaomi", modelo="Xiaomi Note 11", cor="Preto"
)
meu_celular.ligar()
meu_celular.exibirInfo()
