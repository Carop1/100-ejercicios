clave = 0
minutos = 0

print("CLAVES DE DESTINO")
print("[1] Estados unidos - $ 0.13")
print("[2] Canadá - $ 0.11")
print("[5] America del sur - $ 0.52")
print("[6] America central - $ 0.99")
print("[8] Mexico - $ 0.17")
print("[9] Europa - $ 0.17")
print("[10] Asia - $ 0.20")
print("[15] África - $ 0.59")
print("[20] Oceania - $ 0.28")
clave = int(input("Ingrese clave de destino: "))
minutos = int(input("Duracion de la llamada: "))

if(clave == 1):
    print(f"Costo $ {round(minutos*0.13,2)}")
elif(clave ==2):
    print(f"Costo $ {round(minutos*0.11,2)}")
elif(clave ==5):
    print(f"Costo $ {round(minutos*0.52,2)}")
elif(clave ==6):
    print(f"Costo $ {round(minutos*0.99,2)}")
elif(clave ==8):
    print(f"Costo $ {round(minutos*0.17,2)}")
elif(clave ==9):
    print(f"Costo $ {round(minutos*0.17,2)}")
elif(clave ==10):
    print(f"Costo $ {round(minutos*0.20,2)}")
elif(clave ==15):
    print(f"Costo $ {round(minutos*0.59,2)}")
elif(clave ==20):
    print(f"Costo $ {round(minutos*0.28,2)}")
else:
    print("!!Error en clave¡¡")
    
