class Funcionario:
    def __init__(self, dados: dict) -> None:
        # validar entrada de dados e cadastrar funcionário.
        if dados:
            self.nome = dados['nome']
            self.data_nascimento = dados['data_nascimento']
            self.setor = dados['setor']
            self.endereco = dados['endereco']
        else:
            raise Exception('Dados não fornecidos.')

    def cria_user(self) -> str:
        # separa todos os nomes e pegar o primeiro
        nomes = self.nome.split()
        user = nomes[0]

        # pegar todas as iniciais dos sobrenomes
        user += ''.join([i[0] for i in nomes[1:]])

        # transformando a str em minúscula e retornando
        user = user.lower()
        return user

    def format_data(self) -> str:
        # data padrão: dd/mm/aa
        lista_meses = (
            'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
            'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro',
        )

        # separando a data por d/m/a
        dd, mm, aa = self.data_nascimento.split('/')

        # verificando se o mes contem número 0
        if '0' in mm:
            mm = mm.replace('0', '')
            mes = lista_meses[int(mm) - 1]
        else:
            mes = lista_meses[int(mm) - 1]

        # formando a data conforme foi solicitado
        data_formatada = f'{dd} de {mes} {aa}'
        return f'{self.nome} nasceu no dia {data_formatada}'

        # retirando o '0'

    def format_endereco(self):
        # endereço padrão: Rua, número, Bairro, Cidade
        # Os valores são separados por 'virgula'
        rua, numero, bairro, cidade = self.endereco.split(', ')
        endereco_formatado = f'Rua: {rua} \nNúmero: {
            numero} \nBairro: {bairro} \nCidade: {cidade}'

        return endereco_formatado


class Operador(Funcionario):
    def __init__(self, dados: dict, salario: float) -> None:
        if dados and salario:
            super().__init__(dados)
            self.salario = salario
            self._aplicar_reajuste()
        else:
            raise Exception('Dados não fornecidos.')

    # setor de operação deve tirar 33% de reajuste do salário
    def _aplicar_reajuste(self) -> None:
        reajuste = (self.salario * 33) / 100
        self.salario -= reajuste


class Fiscal(Funcionario):
    def __init__(self, dados: dict, salario: float) -> None:
        if dados and salario:
            super().__init__(dados)
            self.salario = salario
            self._aplicar_reajuste()
        else:
            raise Exception('Dados não fornecidos.')

    # setor de fiscalização deve tirar 7% de reajuste do salário
    def _aplicar_reajuste(self) -> None:
        reajuste = (self.salario * 7) / 100
        self.salario -= reajuste
