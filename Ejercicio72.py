clave = 0
usuario = ""

usuario = input("Ingrese usuario: ")
clave = int(input("Ingrese clave:"))

if (usuario =="ADMIN" and clave == 123456):
    print("Acceso permitido")
else:
    print("Acceso denegado")