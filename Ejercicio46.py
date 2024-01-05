H = 0
M = 0
S = 0

H = int(input("Horas:  "))
M = int(input("Minutos:  "))
S = int(input("Segundos:  "))

costo = ((H*3600) + (M*60) + S)*0.25

print(" ")
print(f"Costo total: {costo}")