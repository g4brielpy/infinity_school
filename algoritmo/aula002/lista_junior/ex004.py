x = int(input("Informe o primeiro número: "))
y = int(input("Informe o segundo número: "))
z = int(input("Informe o terceiro número: "))

if x > y :
    print(f"O número {x} é o maior que {y} e {z}")

if y > z :
    print(f"O número {y} é maior que {x} e {z}")

elif x == y and y == z and z == x :
    print("Os números são iguai")

else :
    print(f"O número {z} é maior que {x} e {y}")
