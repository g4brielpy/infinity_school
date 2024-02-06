class Funcionario:
    def __init__(self, dados: dict) -> None:
        self.nome = dados['nome']
        self.data_nascimento = dados['data_nascimento']
        self.setor = dados['setor']
        self.endereco = dados['endereco']