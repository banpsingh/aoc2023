import numpy as np

with open("input.txt", "r") as file:
    data = [list(i) for i in file.read().strip().split("\n")]

expandRow = []
for row in data:
    expandRow.append(row)
    if all(elem == '.' for elem in row):
        expandRow.append(row)

expandCol = []
for row in np.transpose(expandRow):
    expandCol.append(row)
    if all(elem == '.' for elem in row):
        expandCol.append(row)
    
expand = np.transpose(expandCol)

galaxies = {}
count = 1
for i in range(len(expand)):
    for j in range(len(expand[0])):
        char = expand[i][j]
        if char == '#':
            galaxies[count] = (i,j)
            count += 1
res = 0

for i in range(1, len(galaxies)+1):
    for j in range(i+1, len(galaxies)+1):
        x0, y0 = galaxies[i]
        x1, y1 = galaxies[j]
        dist = abs(y1-y0) + abs(x1-x0)
        res += dist

print(res)