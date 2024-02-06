class Funcionario:
    def __init__(self, dados: dict) -> None:
        self.nome = dados['nome']
        self.data_nascimento = dados['data_nascimento']
        self.setor = dados['setor']
        self.endereco = dados['endereco']

    def cria_user(self) -> str:
        # separa todos os nomes e pegar o primeiro
        nomes = self.nome.split()
        user = nomes[0]

        # pegar todas as iniciais dos sobrenomes
        user += ''.join([i[0] for i in nomes[1:]])
        user = user.lower()

        return user

    def format_data(self):
        pass

    def format_endereço(self):
        pass


dados = {
    'nome': 'Gabriel Iuri Dos Santos',
    'data_nascimento': '11/12/2005',
    'setor': 'Fiscal',  # operação ou fiscal
    'endereco': 'Rua Nossa Senhora, 190, Barreiro, Belo Horizonte'
}

biel = Funcionario(dados)
print(biel.cria_user())
