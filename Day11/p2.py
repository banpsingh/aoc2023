import numpy as np

with open("input.txt", "r") as file:
    data = [list(i) for i in file.read().strip().split("\n")]

emptyRows = []
for i in range(len(data)):
    if all(elem == '.' for elem in data[i]):
        emptyRows.append(i)


emptyCols = []
for i in range(len(data[0])):
    if all(elem == '.' for elem in np.transpose(data)[i]):
        emptyCols.append(i)




galaxies = {}
count = 1
for i in range(len(data)):
    for j in range(len(data[0])):
        char = data[i][j]
        if char == '#':
            galaxies[count] = (i,j)
            count += 1

res = 0


for i in range(1, len(galaxies)+1):
    for j in range(i+1, len(galaxies)+1):
        xCount = 0
        yCount = 0
        y0, x0 = galaxies[i]
        y1, x1 = galaxies[j]

        for val in emptyRows:
            if y0>val>y1 or y0<val<y1:
                yCount += 1
        for val in emptyCols:
            if x0>val>x1 or x0<val<x1:
                xCount += 1 

        dist = abs(y1-y0) + yCount*999999 + abs(x1-x0) + xCount*999999
        res += dist

print(res) 