man = 0
noc = 0
tipo = 0
cantidad = 0
bus = 0
van = 0 
micro = 0

print("GANACIAS DE UNA GARITA DE CONTROL")
print("----------------------------------")
cantidad = int(input("CANTIDAD DE VEHICULOS"))
print("")

for cont in range(1,cantidad+1):
    print(">>TIPO DE VEHICULO Nro ",cont, "/", cantidad," : ")
    print("1. Omnibus")
    print("2. Minivan")
    print("3. Micro")
    tipo = int(input("OPCION: "))
    if (tipo ==1):
        tarifa = 13
        bus = bus + tarifa
    elif (tipo ==2):
        tarifa = 10
        van = van + tarifa
    elif (tipo ==3):
        tarifa = 8
        micro = micro + tarifa
    turno = input("Turno (M/N): ")
    if (turno == "M"):
        man = man + tarifa
    else: 
        noc = noc + tarifa
print("Importe de turno mañana: ",man)
print("Importe de turno noche: ",noc)
print("")
print
print("Importe de Omnibus: ",bus)
print("Importe de Minivan: ",van)
print("Importe de Micro: ",micro)

