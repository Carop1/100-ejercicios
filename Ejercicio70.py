n1 = 0
n2 = 0
n3 = 0

n1 = int(input("Ingrese nota 1: "))
n2 = int(input("Ingrese nota 2: "))
n3 = int(input("Ingrese nota 3: "))

prom = (n1 + n2 + n3)/3

if (prom > 10.5):
    print(f"Aprobado con:  {prom}")
else:
    print(f"Desaprobado con: {prom}")