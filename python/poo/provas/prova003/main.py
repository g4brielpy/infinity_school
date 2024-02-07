from fuel import BombaCombustivel


# Menu
MENU = '''
[1] - Abastecer por Valor
[2] - Abastecer por Litro
[3] - Alterar Valor do Litro
[4] - Alterar Tipo de Combustível
[5] - Alterar Quantidade de Combustível
[q] - Sair
-> '''

# Minha bomba de combustível
tipo_combustivel = "Gasolina"
valor_litro = 5.60
quantidade_combustivel = 100.0

bomba = BombaCombustivel(
    tipo_combustivel, valor_litro, quantidade_combustivel)

while True:
    comando = input(MENU)

    match comando:
        case '1':
            try:
                valor_abastecer = float(input("Informe o valor a abastecer: "))
                resultado = bomba.abastecerPorValor(valor_abastecer)
                print(resultado)
            except Exception as e:
                print(f'Erro: {e}')

        case '2':
            try:
                litro_abastecer = float(
                    input("Informe a quantidade de litros a abastecer: "))
                resultado = bomba.abastecerPorLitro(litro_abastecer)
                print(resultado)
            except Exception as e:
                print(f'Erro: {e}')

        case '3':
            try:
                novo_valor = float(input("Informe o novo valor do litro: "))
                bomba.alterarValor(novo_valor)
                print("Valor do litro alterado com sucesso!")
            except Exception as e:
                print(f'Erro: {e}')

        case '4':
            try:
                novo_combustivel = input(
                    "Informe o novo tipo de combustível: ")
                bomba.alterarCombustivel(novo_combustivel)
                print("Tipo de combustível alterado com sucesso!")
            except Exception as e:
                print(f'Erro: {e}')

        case '5':
            try:
                nova_quantidade = float(
                    input("Informe a nova quantidade de combustível: "))
                bomba.alterarQuantidadeCombustivel(nova_quantidade)
                print("Quantidade de combustível alterada com sucesso!")
            except Exception as e:
                print(f'Erro: {e}')

        case 'q':
            break

        case _:
            print("Opção inválida. Tente novamente.")
