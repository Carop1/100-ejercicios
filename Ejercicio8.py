F = 1
C = 1

for F in range(9):
    serie = 0
    for C in range(10-F):
        serie =(serie*10)+C
    print(serie)