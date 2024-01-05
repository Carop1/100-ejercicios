costo = float(input("Costo de la casa: S/> "))
iva = float(input("Valor del IVA en % "))
print(" ")
TotPagar = costo + (costo*(iva/100))
print(f"Iva de {iva}% : S/> {(costo*(iva/100))}")
print(f"Total a pagar: {TotPagar}")

