hor = 0
min = 0
seg = 0
xseg = 0

xseg = int(input("Cantidad de segundos: "))

hor = round(xseg/3600)
min = round((xseg - (hor*3600))/60)
seg = round(xseg - ((hor*3600)+(min*60)))

print(f"Horas: {hor}")
print(f"Minutos: {min}")
print(f"Segundos: {seg}")