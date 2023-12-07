'''
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''



salario = float(input('Digite seu salário: '))
sexo = str(input('Digite seu sexo [F / M]: '))
estado_civil = str(input('Qual seu Estado Civil [S / C / V/ D]: '))

while True:
    # nome
    while True:
        nome = str(input('Digite seu nome: '))
        if (len(nome) < 3):
            print('Valor ivalido!')
        else:
            break
    
    # idade
    while True:
        idade = int(input('Digite sua idade: '))
        if not((idade > 0) and (idade <= 100)):
            print('Valor ivalido!')
        else:
            break