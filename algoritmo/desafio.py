dados_cliente = {
    'nome': '',
    'telefone': '',
    'endereco': '',
}

while True:
    dados_cliente['nome'] = str(input('Digite seu nome: '))
    if (dados_cliente['nome'] == 'FIM'):
        break
    
    dados_cliente['telefone'] = str(input('Digite seu telefone: '))
    dados_cliente['endereco'] = str(input('Digite seu endereço: '))
    

print(dados_cliente)