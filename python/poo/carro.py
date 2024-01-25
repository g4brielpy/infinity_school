# Aprendendo orientação a objeto em python

class Carro:
    def __init__(self, marca: str, modelo: str, ano: str) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print(f'O carro {self.modelo} estar ligado!')

meu_carro = Carro('Fiat', 'Uno', '2009')

print(meu_carro.modelo)
meu_carro.ligar()
'ola'.upper()