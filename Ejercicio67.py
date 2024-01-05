i = 1
j = 1
altura = 0
while((altura % 2) == 0):
    altura = int(input("Altura rombo: "))

for i in range(1,i+1):
    for j in range(1,int((altura-i)/2)+1):
        print(" ", end="")
    
    for j in range(1,i+1):
        print("*",end="")
        
    print("")
for i in range((altura-2),1,-2):
    for j in range(1,int((altura-i)/2)+1):
        print(" ",end="")
    
    for j in range(1,i+1):
        print("*",end="")
    
    print("")