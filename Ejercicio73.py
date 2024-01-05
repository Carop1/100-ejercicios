llamada = 0

llamada = int(input("Cantidad de minutos: "))

if(llamada <= 5):
    costo = llamada*0.9
else:
    costo = (5*0.9) + (llamada -5)*1.1

print(f"El costo es de S/. {costo}")