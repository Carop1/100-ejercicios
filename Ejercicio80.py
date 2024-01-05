print("04. Calcular bonificacion: ")
print("")
venta = float(input("Ingrese monto de la venta: $ "))
if (venta>2000):
    print(f"Bonificacion 10%: $ {venta*0.1}")
else:
    print(f"Bonificacion 50%: $ {venta*0.5}")
    