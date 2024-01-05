cont = 1
n = 0
nota = 0
suma = 0

n = int(input("Ingrese la cantidad de notas:"))

for cont in range(1,n+1):
    nota = float(input(f"Nota: {cont}: "))
    suma = suma + nota
promedio = suma/n
print(f"promedio: {promedio}")