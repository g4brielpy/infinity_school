palavra = str('Gabriel')
c = 0

for vogal in palavra:
    if (vogal in 'a, e, i, o, u'):
        c += 1

print(c)