'''
Nome : pegar o primeiro nome e criar um  nome de user com as primeiras letras dos sobrenomes ex: Otavio Augusto Portela Luciano, deve ficar otavioapl em minusculo.

Data_nascimento: deve separa o dia o mes e o ano e exibir um texto falando o usuario nasceu no dia tal mes [janeiro,fevereiro …] ano xxxx

setor: caso seja setor operação deve tirar 33% do salario dele e informar este desconto e acordo com o salario informado e caso seja fiscal deve tirar 7% e informar o desconto 

endereço : assim como nas datas separe por rua numero bairro e cidade cada dado do associado
'''

import metodos

MENU = '''MENU
[1] - Exibir nome
[2] - Exibir data de nascimento1
[3] - Exibir Endereço
[Q] - Sair
=> '''

# Simulação de entrada de dados padrão
dados = {
    'nome':'Gabriel Iuri Dos Santos',
    'data_nascimento':'11/12/2005',
    'setor': 'fiscal', #operação ou fiscal
    'endereco': 'Rua Nossa Senhora, 190, Barreiro, Belo Horizonte'   
}

while True:
    comando = str(input(MENU).lower())

    match comando:
        case '1':
            print(metodos.formatar_nome(dados['nome']), '\n')
        case '2':
            print(metodos.data_nascimento(dados['data_nascimento']), '\n')
        case '3':
            print(metodos.formatar_endereço(dados['endereco']), '\n')
        case 'q':
            break
        case _:
            print('Opção inválida \n')

