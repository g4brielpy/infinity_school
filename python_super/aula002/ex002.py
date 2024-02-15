notas = [10, 9.8, 3]
media = sum(notas) / len(notas)

if media >= 7:
    print('Aluno passou de ano')
    print(f'Media: {media}')
else:
    print('Reprovo')