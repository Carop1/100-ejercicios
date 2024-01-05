num = 0
c1 = 0
r1 = 0
r2 = 0 
c2 = 0
r2 = 0

num = int(input("Ingrese numero de 3 cifras: "))

c1 = (num - (num%100))/100
r1 =  num % 100
c2 = (r1 - (r1 % 10))/10
r2 = r1 % 10
k = (r2*100) + (c2*10) + c1
if (num == k):
    print("Es un numero capicua")
else: 
    print("No es un numero capicua")