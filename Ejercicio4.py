cont = 0
xpro = 0
pro = 0
xnom = 0
nom = 0

for cont in range(0,5):
    nom = input("Nombre: ")
    pro = float(input("Promedio: "))
    
    if(xpro<pro):
        xpro = pro
        xnom = nom
        
print(f"Alumno con mayor nota:  {xnom}")
print(f"Promedio:  {xpro}")