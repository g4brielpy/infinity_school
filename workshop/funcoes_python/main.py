def paridade(num: int) -> str:
    if num == 0:
        return "Valor inválido"

    if num % 2 == 0:
        return "Par"
    else:
        return "Ímpar"


def numero_primo(num: int):
    primo: bool = True

    if num >= 1:
        for i in range(2, num):
            if num % i == 0:
                primo = False
                break
    else:
        return "Número Inválido!"

    return f"Número {num} é primo" if primo else f"Número {num} não é primo!"


def contar_vogais(frase: str) -> int:
    qtds_vogais: int = 0
    vogais: list = ["a", "e", "i", "o", "u"]

    for letra in frase:
        if letra.lower() in vogais:
            qtds_vogais += 1

    return qtds_vogais


print(numero_primo(0))
