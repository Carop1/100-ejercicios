cont = 0
consumo = 0
total = 0
desc = 0

for cont in range(1,11):
    consumo = int(input(f"Consumo {cont} $. "))
    total = total + consumo
    
if(total>50):
    desc = total*0.07

print(f"Consumo total : $ {total}")
print(f"Descuento : $ {desc}")
print(f"Pago total : $ {total-desc}")

