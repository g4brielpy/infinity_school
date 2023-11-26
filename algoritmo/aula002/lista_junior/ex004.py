x = input("Informe o primeiro número: ")
y = input("Informe o segundo número: ")
z = input("Informe o terceiro número: ")

if x > y :
    print(f"O número {x} é o maior que {y} e {z}")
if y > z :
    print(f"O número {y} é maior que {x} e {z}")
else :
    print(f"O número {z} é maior que {x} e {y}")