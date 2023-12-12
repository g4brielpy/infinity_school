import random

# declarações das variáveis e conjutos
dados_clientes = dict()
clientes = list()
i = True

while (i == True):
    # inputs de coleta de dados
    nome = str(input('\nDigite seu nome: '))
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
print(cliente_sorteado)