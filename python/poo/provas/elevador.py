'''
[PY-A11] Você foi contratado para desenvolver o software de controle de um elevador inteligente. A classe Elevador foi criada para modelar esse sistema e possui os seguintes atributos: totalCapacidade, atualCapacidade, totalAndar e atualAndar, que representam, respectivamente, a capacidade máxima do elevador, a capacidade atual, o total de andares do prédio e o andar atual do elevador.

A classe Elevador também possui os seguintes métodos:

Subir(): caso o elevador não esteja no andar mais alto, o método incrementa o número do andar atual e exibe "Subindo". Caso contrário, exibe "VOCÊ ESTÁ NO ANDAR MAIS ALTO!".

Descer(): caso o elevador não esteja no térreo, o método decrementa o número do andar atual e exibe "Descendo". Caso contrário, exibe "VOCÊ JÁ ESTÁ NO TÉRREO!".

Entrar(): caso a capacidade atual do elevador não tenha sido atingida, o método incrementa o número de pessoas presentes no elevador e exibe "Entrando uma pessoa". Caso contrário, exibe "O ELEVADOR ESTÁ CHEIO!".

Sair(): caso haja pelo menos uma pessoa no elevador, o método decrementa o número de pessoas presentes e exibe "Saindo uma pessoa". Caso contrário, exibe "NÃO TEM NINGUÉM".
'''


class Elevador:
    def __init__(self, total_capacidade: int, atual_capacidade: int, total_andar: int, atual_andar: int) -> None:
        self.total_capacidade = total_capacidade
        self.atual_capacidade = atual_capacidade
        self.total_andar = total_andar
        self.atual_andar = atual_andar

    def Subir(self):
        if self.atual_andar == self.total_andar:
            print('VOCÊ ESTÁ NO ANDAR MAIS ALTO!')
        else:
            print('Subindo')
            self.atual_andar += 1

    def Descer(self):
        if self.atual_andar == 1:
            print('VOCÊ JÁ ESTÁ NO TÉRREO!')
        else:
            print('Descendo')
            self.atual_andar -= 1

    def Entrar(self):
        if self.total_capacidade == self.atual_capacidade:
            print('O ELEVADOR ESTÁ CHEIO!')
        else:
            print('Entrando uma pessoa')
            self.atual_capacidade += 1
    
    def Sair(self):
        if self.atual_capacidade <= 0:
            print('NÃO TEM NINGUÉM')
        else:
            print('Saindo uma pessoa')
            self.atual_capacidade -= 1