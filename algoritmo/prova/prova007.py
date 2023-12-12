'''
- A média de idade de todo o grupo. OK

- Qual o nome da pessoa mais velha. OK

- Quantas pessoas têm menos de 20 anos.

- Quantas pessoas têm mais de 40 anos.

- Qual o sexo da pessoa mais nova.
'''
nome_total = list()
idade_total = list()
idade_max = 0

# estrutura de repetição com 5 loops
for i in range(1, 3):
    nome_input = str(input('Digite seu nome: ').title())
    idade_input = int(input('Digite sua idade: '))
    sexo_input = str(input('Digite seu sexo [F / M]: ').upper())

    dados_pessoais = {
        'nome': nome_input,
        'idade': idade_input,
        'sexo': sexo_input,
    }
    
    
    nome_total.append(dados_pessoais['nome'])
    idade_total.append(dados_pessoais['idade'])

# calculo da media de idades
media_idades = sum(idade_total) / len(idade_total)

# nome da pessoa mais velha / retorna o indice da pessoa
pessoa_velha = max(idade_total)
pessoa_velha = idade_total.index(pessoa_velha)
nome_pessoa_velha = str(nome_total[pessoa_velha])

print(nome_pessoa_velha)



# exibindo as respostas
print(f'A média de idade de todo o grupo é {media_idades}')