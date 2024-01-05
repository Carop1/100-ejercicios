seguro = 0

print("TIPOS DE SEGURO")
print("1. X")
print("2. Y")
print("3. Z")

seguro = int(input("OPCION: "))

if(seguro == 1):
    print("Pago mensual: $45")
elif(seguro ==2):
    print("Pago mensual: $30")
elif(seguro ==3):
    print("Pago mensual: $15")
    
else:
    print("Error en el tipo de seguro")