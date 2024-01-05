meses = 0

monto = 1000

meses = int(input("Nro de meses: "))

intereses = (monto*(meses*0.02))
totalp = monto + intereses

print(f"Intreses: {intereses}")
print(f"Total a pagar: {totalp}")