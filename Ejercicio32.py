x = 0
edad = 0
dia = 0
mes = 0
anio = 0
diax = 30
mesx = 12
aniox = 2023

for x in range(1,11):
    dni = int(input("DNI: "))
    dia = int(input("DIA DE NACIMIENTO: "))
    mes = int(input("MES DE NACIMIENTO: "))
    anio = int(input("AÑO DE NACIMIENTO: "))
    genero = input("GENERO (H/M)")
    print("Fecha actual",diax, "/",mesx,"/", aniox)
    edad = aniox - anio
    if (mes>mesx):
        edad =  edad - 1
    else:
        if(mes==mesx and dia>diax):
            edad = edad -1
    print("EDAD: ",edad, "AÑOS")
    
    if(edad>=8):
        print("Recibe tablet")
    else:
        if (edad == 6):
            if (genero == "H"):
                print("Recibe carrito")
            else:
                print("Recibe muñeca")
            

