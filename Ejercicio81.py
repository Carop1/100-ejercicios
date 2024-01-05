cant = 0
IGV = 0
monto = 0
print("05. Calcular IGV segun el monto de compra")
precio = float(input("Ingrese precio: "))
cant = int(input("Ingrese cantidad: "))
monto = (precio*cant)
if(monto>100):
    IGV = monto*0.18
print("")
print(f"Total:  S/. {monto}")
print(f"IGV 18%:  S/. {IGV}")
print(f"Total a pagar: S/. {(monto+IGV)}")