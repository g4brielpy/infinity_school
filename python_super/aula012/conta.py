# Ex02. Faça uma classe generica chamada "Conta" que terá as seguintes propriedades:
# - titular
# - saldo
# - numero
# e os metódos depositar, sacar e transferir

# Você deve configurar tambés os seguintes tipos de conta
# 1. "ContaCorrente"
# - Terá o atributo cheque_especial
# O metódo sacar / transferir deve considerar o cheque especial

# 2. "ContaPoupanca"
# - Deve ter o atributo "juros_poupanca",
# e também um metódo proprio chamado "corrigir_saldo", que vai adicionar o valor do juros ao saldo.

from random import randint


class Conta:
    def __init__(self, titular: str, saldo: float, numero: str = "") -> None:
        self.titular = titular
        self.saldo = saldo
        self.numero = "".join([str(randint(0, 9)) for i in range(5)])

    def __repr__(self) -> str:
        return f"<Conta - {self.titular}/ N{self.numero}/ R${self.saldo}>"

    def depositar(self, valor: float):
        if valor < 0 and not (isinstance(valor, (float, int))):
            raise ValueError("O valor do deposito é inválido!")

        self.saldo += valor

    def sacar(self, valor: float):
        if valor < 0 and not (isinstance(valor, (float, int))):
            raise ValueError("O valor do deposito é inválido!")

        self.saldo -= valor

    def transferir(self, valor: float, conta: "Conta"):
        self.sacar(valor)
        conta.depositar(valor)
