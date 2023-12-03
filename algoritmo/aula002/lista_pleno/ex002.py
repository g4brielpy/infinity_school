print('F - Feminino')
print('M - Masculino')
sexo = str(input('Informe seu Sexo: '))

if ('F' in sexo) or ('f' in sexo):
    print('Sexo: Feminino')
elif ('M' in sexo) or ('m' in sexo):
    print('Sexo: Masculino')
else:
    print('Sexo inválido!')