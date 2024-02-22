dicionario = {
    'um': 1,
    'dois': 2,
    'três': 3
}
lista = [1, 2, 3, 4, 5, 6]
lista2 = lista[:]

for i, j in zip(lista, lista2):
    print(i, j)
    

print(lista)
print(lista2)
