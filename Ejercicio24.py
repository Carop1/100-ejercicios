num = 0
x = 1
fact = 1

num = int(input("Factorial a calcular: "))

print("Serie del factorial: ")
for x in range(1,num+1):
    y = (num+1)-x
    print(y, end=" ")
    fact = fact * x
print(" ")
print(f"El factorial es: {fact}")