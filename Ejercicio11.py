N = 0
pro = 1
f = 1

N = int(input("Valor de N: "))

for f in range(1,N+1):
    print(f,end=" ")
    pro = pro*f
print("")
print(f"Producto de {N} es {pro}")