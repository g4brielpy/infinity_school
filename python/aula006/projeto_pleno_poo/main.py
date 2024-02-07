'''
Nome : pegar o primeiro nome e criar um  nome de user com as primeiras letras dos sobrenomes ex: Otavio Augusto Portela Luciano, deve ficar otavioapl em minusculo.

Data_nascimento: deve separa o dia o mes e o ano e exibir um texto falando o usuario nasceu no dia tal mes [janeiro,fevereiro …] ano xxxx

setor: caso seja setor operação deve tirar 33% do salario dele e informar este desconto e acordo com o salario informado e caso seja fiscal deve tirar 7% e informar o desconto 

endereço : assim como nas datas separe por rua numero bairro e cidade cada dado do associado
'''

import employee

# Simulação de entrada de dados padrão
dados = {
    'nome': 'Gabriel Iuri Dos Santos',
    'data_nascimento': '11/12/2005',
    'setor': 'Fiscal',  # operação ou fiscal
    'endereco': 'Rua Nossa Senhora, 190, Barreiro, Belo Horizonte'
}
if dados['setor'].lower() == 'fiscal':
    salario = float(2000)
    funcionario = employee.Fiscal(dados, salario)
elif dados['setor'].lower() == 'operador':
    salario = float(5000)
    funcionario = employee.Operador(dados, salario)
else:
    funcionario = employee.Funcionario(dados)

MENU = '''MENU
[1] - Exibir User
[2] - Exibir Data De Nascimento
[3] - Exibir Endereço
[4] - Exibir Setor
[Q] - Sair
=> '''


while True:
    comando = str(input(MENU)).lower()
    match comando:
        case '1':
            print(funcionario.cria_user())
        case '2':
            print(funcionario.format_data())
        case '3':
            print(funcionario.format_endereco())
        case '4':
            print(funcionario.setor)
            print(type(funcionario))
        case 'q':
            print('Programa finalizado')
            break
        case _:
            print('Opção inválida!\n')
