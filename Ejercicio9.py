C = 0
F = 1
XN = 7

for F in range(9):
    serie = " "
    if (F >= 5):
        XN = XN + 2
    for C in range(XN-F):
        serie = serie + "*"
    print(serie)
