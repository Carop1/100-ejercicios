print("MENU DE OPCIONES DE UN TRIANGULO")
print("---------------------------------")
print("1. Area de un triangulo, dada la base y la altura")
print("2. Base de un triangulo, dada la altura y el area")
print("3. Altura de un triangulo, dada la base y el area")
OPC = int(input("Selecciona una opcion: "))

print("")

if (OPC == 1):
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    area = (base*altura)/2
    print(f"El area es: {area}")
elif (OPC == 2):
    altura = float(input("Altura: "))
    area = float(input("Area: "))
    print("OPC VERDE")
    base = (area*2)/altura
    print(f"La base es: {base}")
elif (OPC == 3):
    base = float(input("Base: "))
    area = float(input("Area: "))
    altura = (area*2)/base
    print(f"La altura es: {altura}")
else:
    print("Error... opcion incorrecta")