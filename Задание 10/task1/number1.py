import random
import os
absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)

with open(path + "\\vvod.txt") as f:
    matrix = [list(map(int, row.split())) for row in f.readlines()]
    print(matrix)

pol = 0
s = 0


def area(mtrx):
    pol = 0
    s = 0

    for i in range(len(mtrx)):
        for j in range(i+1, len(mtrx)):
            if mtrx[i][j] <= 0:
                continue
            if mtrx[i][j] > 0:
                pol += 1
                s += mtrx[i][j]

    print('Сумма:', s)
    print('Число:', pol)
    file = open(path + "\\vivod.txt", "w")
    file.write('Сумма: ' + str(s) + '\n')
    file.write('Число: ' + str(pol))
    file.close()

area(matrix)