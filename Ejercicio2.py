cont = 0
num = 0
par = 0
impar = 0

print("Escriba el listado de numeros")
for cont in range(0,10):
    num = int(input(f"Numero {cont}: "))
    if (num % 2 == 0):
        par = par +1
    else:
        impar = impar + 1
print(f"Cantidad de pares: {par}")
print(f"Cantidad de impares: {impar}")