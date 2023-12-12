import random

# declarações das variáveis e conjutos
dados_clientes = dict()
clientes = list()
i = True

while (i == True):
    print('\nNOVO CLIENTE\n')
    # inputs de coleta de dados
    nome = str(input('Digite seu nome: '))
    if (nome.upper() == 'FIM'):
        break
    telefone = str(input('Digite seu telefone: '))
    endereco = str(input('Digite seu endereço: '))

    # dados de clientes
    dados_clientes = {
        'nome': nome,
        'telefone': telefone,
        'endereço': endereco
    }

    # armazenando todos os crientes
    clientes.append(dados_clientes)

    # verificar se há mais clientes
    while True:
        i = str(input('\nDeseja continuar [S / N]: '))
        if (i.upper() == 'S'):
            i = True
            break
        elif (i.upper() == 'N'):
            i = False
            break
        else:
            print('Valor inválido!')

# sorteio do cliente e adicionado os dados em um dict
cliente_sorteado = dict(random.choice(clientes))

# exibindo o cliente sorteado
print('\nSORTEIO\n')

print(f'O cliente soteado: {cliente_sorteado['nome'].title()}')
print(f'O telefone dele: {cliente_sorteado['telefone']}')
print(f'O endereço dele: {cliente_sorteado['endereço'].title()}\n')

print('FIM')