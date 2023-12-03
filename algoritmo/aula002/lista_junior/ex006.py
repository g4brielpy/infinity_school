palavra = str(input('Digite uma palavra: '))

if 'a' in palavra or 'A' in palavra:
    print(f'Na palavra {palavra} tem letra A')
else:
    print(f'Na palavra {palavra} não tem letra A')