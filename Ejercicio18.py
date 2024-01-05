num = input("Ingrese un numero: ")
tem = []

for i in range(len(num)-1, -1, -1):
    tem.append(num[i])

tem = int(''.join(tem))

print("")
print(f"Numero ingresado: {num}")
print(f"Numero cambiado:  {tem}")

if num == str(tem):
    print("Si es un numero Capicúa")
else:
    print("No es un numero Capicúa")

