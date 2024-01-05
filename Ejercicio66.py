alt = int(input("ingrese altura del triangulo: "))
caract = input("Ingrese un caracter: ")

for i in range(1,alt+1):
    for j in range(1,(alt-i)+1):
        print(" ",end="")
        
    for j in range(1,((i*2)-1)+1):
        print(caract,end="")
    
    print("")