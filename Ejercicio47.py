mes = 0
dia = 0
tiempo = 0

mes = int(input("Nro de mes: "))
dia = int(input("Nro de dias: "))

tiempo = (((mes - 1)*30) + dia)

print(" ")
print(f"Los dias transcurridos son: {tiempo}")