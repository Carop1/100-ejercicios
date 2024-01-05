import random
color = 0
desct = 0
compra = 0

compra = float(input("Valor de compra: S/. "))
tecla = input()
color = random.randint(1,5)

if (color == 1):
    print("Color BLANCO")
    desct = 1
elif (color == 2):
    print("Color VERDE")
    desct = 0.5
elif (color == 3):
    print("Color NEGRO")
    desct = 0.4
elif (color == 4):
    print("Color CELESTE")
    desct = 0.05
elif (color == 5):
    print("Color ROJO")
    desct = 0
print(f"Descuento: S/. ", desct)
print(f"Importe descuento: S/. ")
print("Pago final: S/. " , compra - (compra*desct))