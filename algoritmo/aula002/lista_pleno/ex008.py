data_input = input("Digite uma data no formato dd/mm/aaaa: ")

# Divide a string da data
data_parts = data_input.split('/')
dia, mes, ano = map(int, data_parts)

if (dia >= 1 and dia <= 31) and (mes >= 1 and mes <= 12) and (ano <= 2021):
    print('Data válida!')
else:
    print('Data inválida!')