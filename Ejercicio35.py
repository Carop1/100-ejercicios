x = 0
z = 0
num = 0
val = 1
f = 0

print("MUESTRA GRAFICA DE NUMEROS COMO UN TRIANGULO")

while (num<3):
    num = int(input("Ingrese numero mayor o igual a 3"))
    
print("")

print("")

for x in range(1, num + 1):
    espa = " " * (num - x)
    print(espa, end="")
    contador = 1

    for f in range(1, 2 * x):
        print(contador, end="")
        if contador == 9:
            contador = 0
        else:
            contador += 1

    print("")