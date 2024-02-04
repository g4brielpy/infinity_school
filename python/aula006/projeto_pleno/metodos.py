# NOME
def formatar_nome(nome):
    lista_nome = nome.split()
    nome_formatado = lista_nome[0]

    for i in lista_nome:
        if not i == nome_formatado:
            nome_formatado += ''.join(i[0])
    
    return nome_formatado.lower()


def data_nascimento(data):
    lista_meses = {
        '1': 'janeiro',
        '2': 'fevereiro',
        '3': 'março',
        '4': 'abril',
        '5': 'maio',
        '6': 'junho',
        '7': 'julho',
        '8': 'agosto',
        '9': 'setembro',
        '10': 'outubro',
        '11': 'novembro',
        '12': 'dezembro',
    }
    dia, mes, ano = data.split('/')
    mes = lista_meses[mes]
    data_formatada = f'{dia} {mes} {ano}'

    return data_formatada
    

def formatar_endereço(endereco):
    rua, numero, bairro, cidade = endereco.split(', ')
    endereco_formatado = f'''Rua: {rua}\nNumero: {numero}\nBairro: {bairro}\nCidade: {cidade}'''
    return endereco_formatado
