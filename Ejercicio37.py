print("MOSTRAR EL TRIANGULO DE PASCAL")
# Initialize the matrix M
N = int(input("Entre la dimesion de la matriz: "))
M = [[0] * N for _ in range(N)]


for i in range(N):
    M[i][0] = 1  # 
    M[i][i] = 1  # 

for i in range(2, N):
    for j in range(1, i):
        M[i][j] = M[i - 1][j] + M[i - 1][j - 1]

for i in range(N):
    spaces = " " * (N - i - 1)
    print(spaces, end="")
    for j in range(i + 1):
        val = M[i][j]
        if val != 0:
            print(val, end=" ")
    print("")