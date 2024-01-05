divisi = 0

num = int(input("Ingrese numero: "))

for divi in range(2,num):
    if(num % divi) == 0:
        divisi = divisi + 1
if (divisi == 0):
    print("Numero primo")
else:
    print("No es primo")
    