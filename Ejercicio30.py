ventas = 0
empleados = 0
tv_h = 0
tv_m = 0
muj = 0
nomb = ""
genero = ""

empleados = int(input("Cantidad de empleados: "))
Print = " "

for cont in range(1, empleados+1):
    print(f"Empleado Nro {cont} / {empleados}")
    nom = input("Nombre: ")
    genero = input("Genero (H/M): ")
    ventas = int(input("Ventas: "))
    print(" ")
      
    if (genero == "H"):
        tv_h = tv_h + ventas
    else:
        tv_m = tv_m + ventas
        muj = muj + 1
print(f"Total de ventas hombre: {tv_h}")
print(f"Total de ventas mujeres: {tv_m}")
print(" ")
print(f"Porcentaje de mujeres: ", (muj*100)/empleados)