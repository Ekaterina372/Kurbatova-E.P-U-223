import random

import os
absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)

with open(path +"\\vvod.txt") as f:
    matrix = [list(map(int, row.split())) for row in f.readlines()]
    print(matrix)


N = len(matrix)
M = len(matrix[0])

def result(matrix):
    for i, row in enumerate(matrix):
        max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[0], row[len(matrix)-1] = row[min], row[max]


    return matrix


with open(path +"\\vivod.txt", "w") as f:
        for line in result(matrix):
            for elem in line:
                f.write(str(elem) + " ")
            f.write('\n')