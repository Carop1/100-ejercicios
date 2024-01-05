import random
i = 0
numA = random.randrange(0,20)
num = 0
sw = 0


for i in range(3):
    num = int(input("Encuentre el numero entre 0 y 20: "))
    if (num == numA):
        print("Numero encontrado")
        sw = 1
        i = 3
        
    else:
        if (num>numA):
            print("Ingrese un numero menor")
        else:
            print("Ingrese un numero mayor")
    print(" ")
if(sw == 0):
    print(f"El numero a encontrar era: {numA}")