print("Mostrar el porcentaje de alumnos aprobados y desaprobados")
print("")
apro = int(input("Ingrese la cantidad de alumnos aprobados: "))
desa = int(input("Ingrese la cantidad de alumnos desaprobados: "))
print("")

porA = round((apro*100)/(apro + desa),2)
porD = round((desa*100)/(apro + desa),2)

print(f"Aprobados : {porA} %")
print(f"Desaprobados : {porD} %")