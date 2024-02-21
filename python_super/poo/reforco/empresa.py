class CadastroEmpresa:
    total_empresa = 0

    def __init__(self, razao_social: str, responsavel: str, rendimento_anual: float,
                 qntd_funcionario_clt: int) -> None:
        self.razao_social = razao_social
        self.responsavel = responsavel
        self.rendimento_anual = rendimento_anual
        self.funcionarios = qntd_funcionario_clt
        self.situacao_empresa = False

    def exibirInformacoes(self) -> None:
        print(f'Nome da Empresa: {self.razao_social}')
        print(f'Responsável da Empresa: {self.responsavel}')
        print(f'Rendimento Anual: {self.rendimento_anual}')
        print(f'Quantidade de Funcionários CLT: {self.funcionarios}')
        self.situacaoEmpresa()

    def avaliacaoCredito(self) -> None:
        if self.situacao_empresa and self.rendimento_anual >= 100_000.00:
            print(f'Limite de crédito: {self.rendimento_anual * 0.75}')
        else:
            print('Não há limite de crédito')

    def situacaoEmpresa(self) -> None:
        print('Empresa Ativa' if self.situacao_empresa else 'Empresa Inativa')

    def ativarCadastroEmpresa(self) -> None:
        self.situacao_empresa = True

    def desativarCadastroEmpresa(self) -> None:
        self.situacao_empresa = False


my_empresa = CadastroEmpresa(razao_social='Santos', responsavel='Gabriel Iuri',
                             rendimento_anual=150_000.00, qntd_funcionario_clt=10)

my_empresa.exibirInformacoes()
my_empresa.avaliacaoCredito()
