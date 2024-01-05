num = 0
DEC = 0
UNI = 0
DECENA = 0
UNIDAD = 0
print("PASAR DE NUMEROS A LETRAS")

num = int(input("Ingrese numero de hasta 2 cifras: "))

if (num>0 and num<100):
    if (num>10 and num<16):
       if (num == 11):
        print("ONCE")
    
       elif (num == 12):
            print("DOCE")
        
       elif (num == 13):
            print("TRECE") 
       elif (num == 14):
            print("CATORCE")
        
       elif (num == 15):
            print("QUINCE") 
    
    else:
        DEC = (num - (num%10))/10
        UNI = (num%10)
        if(DEC ==1):
            DECENA = "DIEZ"
        elif (DEC == 2):
            DECENA = "VEINTE"
        elif (DEC == 3):
            DECENA = "TREINTA"
        elif (DEC == 4):
            DECENA = "CUARENTA"
        elif (DEC == 5):
            DECENA = "CINCUENTA"
        elif (DEC == 6):
            DECENA = "SESENTA"
        elif (DEC == 7):
            DECENA = "SETENTA"
        elif (DEC == 8):
            DECENA = "OCHENTA"
        elif (DEC == 9):
            DECENA = "NOVENTA"
        if(UNI != 0):
            if(UNI==1):
                UNIDAD = "UNO"
            elif(UNI == 2):
                UNIDAD = "DOS"
            elif(UNI == 3):
                UNIDAD = "TRES"
            elif(UNI == 4):
                UNIDAD = "CUATRO"
            elif(UNI == 5):
                UNIDAD = "CINCO"
            elif(UNI == 6):
                UNIDAD = "SEIS"
            elif(UNI == 7):
                UNIDAD = "SIETE"
            elif(UNI == 8):
                UNIDAD = "OCHO"
            elif(UNI == 9):
                UNIDAD = "NUEVE"
            if (DEC == 1):
                DECENA = "DIECI"
            if(DEC == 2):
                DECENA = "VENTI"
            if(DEC>2 and DEC<10):
                print(f"{DECENA} y {UNIDAD}")
            else:
               print(DECENA,"", UNIDAD)
        else: 
            print(DECENA)
else:
    print("Numero incorrecto")
        
            
      
        