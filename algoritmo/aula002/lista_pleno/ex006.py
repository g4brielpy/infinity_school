print('Em qual turno voce estuda ?')
print('M - matutino // V - Vespertino // N - Noturno')
turno = str(input('Digite o turno: '))

if (turno == 'm') or (turno == 'M'):
    print('Bom Dia!')
elif (turno == 't') or (turno == 'T'):
    print('Boa Tarde!')
elif (turno == 'n') or (turno == 'N'):
    print('Boa Noite!')
else:
    print('Turno invalido!')