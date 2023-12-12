# lista de daddos
lista_nomes = list()
lista_idades = list()
lista_sexos = list()

pessoas_novas = 0
pessoas_velhas = 0

# loop de coleta de dados de 5 pss
for i in range(5):
    nome = str(input('\nDigite seu nome: ').title())
    idade = int(input('Digite sua idade: '))
    while True:
        sexo = str(input('Digite seu sexo [F / M]: ').upper())
        if (sexo == 'F'):
            sexo = 'Feminino'
            break
        elif (sexo == 'M'):
            sexo = 'Masculino'
        else:
            print('Valor inválido!\n')

    # atribuindo os valores as lista
    lista_nomes.append(nome)
    lista_idades.append(idade)
    lista_sexos.append(sexo)

# média de idadde do grupo / média de inteiro
media_idades = sum(lista_idades) // len(lista_idades)

# pessoa mais velha
maior_idade = lista_idades.index(max(lista_idades))
nome_pessoa_velha = lista_nomes[maior_idade]

# pessoas com menos de 20 anos
for i in lista_idades:
    if (i < 20):
        pessoas_novas += 1

# pessoas com mais de 40 anos
for i in lista_idades:
    if (i > 40):
        pessoas_velhas += 1

# sexo da pessoa mais nova
menor_idade = lista_idades.index(min(lista_idades))
sexo_pessoa_nova = lista_sexos[menor_idade]

# Exibir os resultados
print("\nGRUPO:")
print(f"Média de idade do grupo: {media_idades} anos")
print(f"Pessoa mais velha: {nome_pessoa_velha.title()}")
print(f"Pessoas com menos de 20 anos: {pessoas_novas}")
print(f"Pessoas com mais de 40 anos: {pessoas_velhas}")
print(f"Sexo da pessoa mais nova: {sexo_pessoa_nova}")