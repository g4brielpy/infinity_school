'''
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
'''

from random import choice


def escolher_palavra() -> str:
    palavras = ["python", "programacao",
                "desenvolvimento", "openai", "inteligencia"]
    return choice(palavras)


PALAVRA: str = escolher_palavra()
exibicao = ['_' for letra in PALAVRA]
tentativas_disponiveis = 6

while True:
    print('\n----- JOGO DA FORCA -----')
    print(f'Tentativas disponíveis: {tentativas_disponiveis}')
