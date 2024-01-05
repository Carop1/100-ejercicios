nom = ""
hijos = 0
boni = 0
sueldof = 0

print("Calcular el sueldo final")
nom = input("Ingrese nombre: ")
sueldoB = float(input("Sueldo basico: S/. "))
hijos = int(input("Nro. de hijos: "))

if (hijos>0):
    boni = round(sueldoB*0.7,1)
    sueldof = sueldoB+boni
print("")
print(f"Bonificacion: S/. {boni} ")
print(f"Sueldo final: S/. {sueldof}")