num1 = 0
num2 = 0
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
print("Operador")
operador = int(input("[1. +][2. -][3. x][4. /]: "))

if(operador == 1):
    print("Suma: ", num1 + num2)
elif(operador ==2):
    print("Resta: ",num1 - num2)
elif(operador ==3):
    print("Multiplicacion: ", num1 * num2)
elif(operador ==4):
    print("Division: ",num1 / num2)
else:
    print("Operador incorrecto")