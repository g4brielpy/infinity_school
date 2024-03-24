class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def getNome(self) -> str:
        return f"Meu nome é {self.nome}"

    def enviarMensagem(self) -> str:
        return f"Enviando mensagem para {self.nome} no telefone {self.telefone}"


clientes: list = [
    Cliente(
        nome="Gabriel", cpf="000.000.000-00", telefone="319999-9999"
    ),
    Cliente(
        nome="Iuri", cpf="111.111.111-11", telefone="318888-8888"
    ),
    Cliente(
        nome="Santos", cpf="222.222.222-22", telefone="317777-7777"
    )
]

for cliente in clientes:
    print(cliente.enviarMensagem() + "\n")
