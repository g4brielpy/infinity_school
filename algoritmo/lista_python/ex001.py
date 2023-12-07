while True:
    nota = str(input('Digite uma nota entre 0 e 10: '))

    if (nota.isdigit()):
        nota = int(nota)

        if (nota >= 0) and (nota <= 10):
            print(f'Nota {nota} válida!')
            break
        else:
            print(f'Valor {nota} inválido, digite um número de 0 a 10 \n')
    else:
        print('Por favor, digite um valor numérico inteiro.\n')