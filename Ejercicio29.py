sumaP = 0
sumaI = 0

num = int(input("Ingrese numero: "))

for x in range(1,num+1):
    if (x%2)== 0:
        sumaP = sumaP + x
    elif ( x%2)==1:
        sumaI = sumaI + x
print(f"Suma de pares: {sumaP}")
print(f"Suma de impares: {sumaI}")
         
    
         