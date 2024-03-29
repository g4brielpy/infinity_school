'''
Classe BombaCombustível:
Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses ATRIBUTOS:
    i.TipoCombustivel. OK
    ii.ValorLitro. OK
    iii.QuantidadeCombustivel. OK

Possua no mínimo esses MÉTODOS:

    1.abastecerPorValor( )
        método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo

    2.abastecerPorLitro( )
        método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.

    OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba

    3. alterarValor( )
        altera o valor do litro do combustível.

    4. alterarCombustivel( )
        altera o tipo do combustível.

    5.  alterarQuantidadeCombustivel( )
        altera a quantidade de combustível restante na bomba.
'''


class BombaCombustivel:
    def __init__(self, tipo_combustivel: str, valor_litro: float, quantidade_combustivel: float) -> None:
        """
        Inicializa a bomba de combustível com os atributos fornecidos.
        """
        if tipo_combustivel and valor_litro > 0 and quantidade_combustivel > 0:
            self.combustivel = str(tipo_combustivel)
            self.valor_litro = float(valor_litro)
            self.quantidade = float(quantidade_combustivel)
        else:
            raise Exception('Dados inválidos.')

    def abastecerPorValor(self, valor_abastecer: float) -> str:
        """
        Abastece a quantidade de litros correspondente ao valor fornecido.
        Retorna uma mensagem indicando o sucesso ou falha da operação.
        """
        litros_abastecer = valor_abastecer / self.valor_litro

        if self.quantidade >= litros_abastecer:
            self.quantidade -= litros_abastecer
            return f'Valor a ser abastecido: {valor_abastecer:,.2f}  \nQuantidade de litros: {litros_abastecer:,.2f}'
        else:
            return f'Falha! Quantidade de litros indisponível'

    def abastecerPorLitro(self, litro_abastecer: float) -> str:
        """
        Abastece a quantidade de litros fornecida.
        Retorna uma mensagem indicando o sucesso ou falha da operação.
        """
        if self.quantidade >= litro_abastecer:
            custo = litro_abastecer * self.valor_litro

            self.quantidade -= litro_abastecer
            return f'Valor a ser abastecido: {custo:,.2f} \nQuantidade de litros: {litro_abastecer:,.2f}'
        else:
            return f'Falha! Quantidade de litros indisponível'

    # Setters
    def alterarValor(self, novo_valor: float) -> None:
        """
        Altera o valor do litro do combustível.
        Levanta uma exceção se o novo valor for inválido.
        """
        if novo_valor > 0:
            self.valor_litro = novo_valor
        else:
            raise Exception('Valor inválido para o litro do combustível.')

    def alterarCombustivel(self, novo_combustivel: str) -> None:
        """
        Altera o tipo combustível.
        Levanta uma exceção se o novo tipo não for informado.
        """
        if novo_combustivel:
            self.combustivel = novo_combustivel
        else:
            raise Exception('Combustível inválido.')

    def alterarQuantidadeCombustivel(self, nova_quantidade: float) -> None:
        '''
        Altera a quantidade do combustivel
        Lavanta uma exceção caso o quantidade seja abaixo de zero
        '''
        if nova_quantidade > 0:
            self.quantidade = nova_quantidade
        else:
            raise Exception('Valor inválido para a quantidade do combustível.')
