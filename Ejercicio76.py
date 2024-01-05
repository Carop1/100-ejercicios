n1 = 0
n2 = 0
n3 = 0
medio = 0
xtem = 0

n1 = int(input("Ingrese numero 1: "))
n2 = int(input("Ingrese numero 2: "))
n3 = int(input("Ingrese numero 3: "))

if (n1>n2):
    medio = n1
    xtem = n2
else:
    medio = n2
    xtem = n1

if (medio>n3):
    medio=n3
if(medio<xtem):
    medio = xtem
print(f"El numero medio es: {medio}")