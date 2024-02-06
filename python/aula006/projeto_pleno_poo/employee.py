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

    # setor operação deve tirar 33% do salário
    def _aplicar_reajuste(self) -> None:
        reajuste = (self.salario * 33) / 100
        self.salario -= reajuste


class Fiscal(Funcionario):
    pass


# entrada de dados padrão
dados = {
    'nome': 'Gabriel Iuri Dos Santos',
    'data_nascimento': '11/12/2005',
    'setor': 'Fiscal',  # operação ou fiscal
    'endereco': 'Rua Nossa Senhora, 190, Barreiro, Belo Horizonte'
}

dados_operador = {
    'nome': 'Iuri dos Santos',
    'data_nascimento': '01/01/1990',
    'setor': 'Operacao',
    'endereco': 'Rua Principal, 123, Centro, Contagem'
}

# teste
try:
    print('\nClass Funcionário')
    biel = Funcionario(dados)

    print(biel.cria_user())
    print(biel.format_data())
    print(biel.format_endereco())

    print('\nClass Operador')
    operador_iuri = Operador(dados_operador, 5000)
    print(operador_iuri.cria_user())
    print(operador_iuri.format_data())
    print(operador_iuri.format_endereco())


except Exception as e:
    print(f'Valores inválidos. Exceção: {e}')
