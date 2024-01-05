
num = int(input("Ingrese un valor: "))
for cont in range(2,num):
    divisible = 0
    for divi in range(1,cont+1):
        k = cont % divi
        if(k == 0):
            divisible = divisible + 1
    if (divisible == 2):
        print(cont, end = " ")
    divisible = 0
print(" ") 
