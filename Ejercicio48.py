

num = int(input("Ingrese Nro. de 3 cifras:  "))

cent = (num - (num % 100))/100
res = num%100
dec = (res -(res%10))/10
uni = res%10

print("")
print(f"Centena: {cent}")
print(f"Decena: {dec}")
print(f"Unidad: {uni}")
