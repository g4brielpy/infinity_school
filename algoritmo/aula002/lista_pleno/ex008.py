data_input = input("Digite uma data no formato dd/mm/aaaa: ")

# Divide a string da data
data_parts = data_input.split('/')
dia, mes, ano = map(int, data_parts)