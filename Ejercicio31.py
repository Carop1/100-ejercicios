C = 0
S = 0 
D = 0
L = 0
R = 0
M = 0
ref = ""
consonante = 0
refran = ""

ref = input(f"Ingrese refran: ")

for F in range(len(ref)+1):
    k =[ref,F,F]
    if (k != " "):
        refran = refran + k
print(refran)
for F in range(1,len(refran)+1):
    refran = refran.join()
    refran = refran.upper()
    v = [refran,F,F]
    
    
    #letra = v.upper()
    
    