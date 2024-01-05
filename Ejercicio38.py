r = 0
v = 0
a = 0

N = int(input("CANTIDAD DE PERSONAS: "))

for i  in range(1,N+1):
    print(f"PERSONA Nro, {i} ",end="")
    c = ""
    while (c != "ROJO" and c!= "VERDE" and c != "AZUL"):
        c = input("[ROJO - VERDE - AZUL]: ")
        c = c.upper()
    if (c== "ROJO"):
        r = r + 1
    else:
        if (c=="VERDE"):
            v = v + 1
        else:
            a = a +1
print("")
if(r>v and r> a):
    Mcolor = "ROJO"
else:
    if(v >r and v>a):
        Mcolor = "VERDE"
    else:
        Mcolor = "AZUL"
        
print(f"Cantidad de color rojo: {r}")
print(f"Cantidad de color verde: {v}")
print(f"Cantidad de color azul: {a}")
print(f"El color mas escogido: {Mcolor}")

