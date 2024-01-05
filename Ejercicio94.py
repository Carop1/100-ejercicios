categoria = 0
bonificacion = 0
sueldo = int(input("Sueldo base S/. "))
categoria = int(input("Categoria: 1. A - 2. B - 3. C - 4. D: "))

if (categoria == 1):
    bonificacion = sueldo*0.1
elif (categoria == 2):
    bonificacion = sueldo*0.2
elif (categoria == 3):
    bonificacion = sueldo*0.3
elif (categoria ==4):
    bonificacion = sueldo*0.5
    
print(f"Bonificacion: S/. {bonificacion}")
print(f"Sueldo neto: S/. {sueldo+bonificacion}")

    
             
