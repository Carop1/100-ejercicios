A = 0
B = 0

A = int(input("Numero A: "))
B = int(input("Numero B: "))

if (A<B):
    N = A+1
    for N in range(N,B):
        print(N)
else:
    N = B+1
    for N in range(N,A):
        print(N)   