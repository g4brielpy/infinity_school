salario_atual = float(input('Informe seu salário atual: R$ '))

if (salario_atual <= 280): 
    reajuste = 20
elif (salario_atual <= 700):
    reajuste = 15
elif (salario_atual <= 1500):
    reajuste = 10
elif (salario_atual > 1500):
    reajuste = 5
else:
    print('Valor invalido!')

valor_reajuste = (salario_atual * reajuste) / 100
salario_novo = (salario_atual + valor_reajuste)

print(f'\nSalário antes do reajuste: R$ {round(salario_atual, 2)}')
print(f'O percentuado do aumento foi de {round(reajuste, 0)}%')
print(f'O valor do aumento foi de R$ {round(valor_reajuste, 2)}')
print(f'Salário após o reajuste: R$ {round(salario_novo, 2)}')