
monto = float(input("MOnto de compra: S/. "))

if monto >=350:
    desct = monto*0.35
    print(f"El descuento es de 35%: S/. {desct}")
else:
    desct = monto*0.1
    print(f"Descuento es de un 10%: S/. {desct}")

print(f"Monto a cancelar: S/. {monto-desct}")