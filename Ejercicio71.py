num = 0
c = 0
r = 0
re = 0

num = int(input("Ingrese un numero: "))

c = round(num/2)
r = c*2
re = num -r

if  (re == 0 ):
    print("Numero par")
else:
    print("Numero impar")