N1 = 0
N2 = 0
N3 = 0

N1 = int(input("Ingrese nota 1: "))
N2 = int(input("Ingrese nota 2: "))
N3 = int(input("Ingrese nota 3: "))

prom = round((N1 + N2 + N3)/3)
print("Pormedio : ", prom)
if (prom >=1 and prom<=10):
    print("Nivel malo")
elif (prom >= 11 and prom <= 13):
    print("Nivel regular")
elif (prom >= 14 and prom <= 16):
    print("Nivel bueno")
elif (prom >=  17 and prom <= 20):
    print("Nivel muy bueno")
