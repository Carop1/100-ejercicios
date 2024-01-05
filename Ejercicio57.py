dias = int(input("Ingrese Cantidad de dias: "))

A = round(dias/365)
M = round((dias - (A*365))/30)
D = round(dias - ((A*365) + (M*30)))

print(f"Año: {A}")
print(f"Mes: {M}")
print(f"Dia: {D}")