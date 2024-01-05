cont = 0
a = 0
e = 0
i = 0
oo = 0
u = 0

vocal = ""

frase = input("Frase: ")
frase = frase.upper()
for cont in range(0,len(frase)):
    vocal = frase[cont]
    if(vocal =="A" or vocal=="Á"):
        a = a + 1
    if(vocal =="E" or vocal=="É"):
        e = e + 1
    if(vocal =="I" or vocal=="Í"):
        i = i + 1    
    if(vocal =="O" or vocal=="Ó"):
        oo = oo + 1
    if(vocal =="U" or vocal=="Ú"):
        u = u + 1
print("Cantidad de vocales")
print("A: ",a)
print("E: ",e)
print("I: ",i)
print("O: ",oo)
print("U: ",u)