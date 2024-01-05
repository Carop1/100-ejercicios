sueldoBase = 0
num_hijos = 0
dias_no_laborales = 0
sueldo_final = 0

print("CALCULAR EL SUELDO FINAL DE UN EMPLEADO")
print("")
sueldoBase = int(input("Ingrese el sueldo base : $ "))
num_hijos = int(input("Ingrese el numero de hijos: "))
dias_no_laborales = int(input("Ingresar dias no laborales trabajados"))

sueldo_final = sueldoBase + num_hijos*100 + (dias_no_laborales*25)

print("")
print(f"Sueldo final: {sueldo_final}")