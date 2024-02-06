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

    def format_data(self) -> str:
        # lista com todos os meses
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

    def format_endereço(self):
        pass

# entrada de dados padrão
dados = {
    'nome': 'Gabriel Iuri Dos Santos',
    'data_nascimento': '11/12/2005',
    'setor': 'Fiscal',  # operação ou fiscal
    'endereco': 'Rua Nossa Senhora, 190, Barreiro, Belo Horizonte'
}

# teste
try:
    biel = Funcionario(dados)

    print(biel.cria_user())
    print(biel.format_data())
    
except Exception as e:
    print(f'Valores inválidos. Exceção: {e}')

