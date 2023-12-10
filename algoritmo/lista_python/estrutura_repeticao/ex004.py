'''
Supondo que a população de um país 

'A' seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de 
'B' seja 200000 habitantes com uma taxa de crescimento de 1.5%. 

Faça um programa que calcule e escreva o número de ANOS necessários para que a população do país 'A' ULTRAPASSE ou iguale a população do país 'B', mantidas as taxas de crescimento.
'''
pais_A = 80000
pais_B = 200000
anos = 0

while pais_A <= pais_B:
    pais_A += pais_A * (3/100) # 3%
    pais_A += pais_B * (1.5/100) # 1.5%

    anos += 1

print(f"Levará {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")