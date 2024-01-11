#7309459565207

from math import lcm
with open("input.txt", "r") as file:
    instruc, data = file.read().split("\n\n")

data = data.split("\n")

startNodes = []

network = {}
for row in data:
    node, rest = row.split(" = ")
    if node[-1] == 'A': startNodes.append(node)
    left, right = rest.split(", ")
    left, right = left[1:], right[:-1]
    network[node] = (left, right)


steps = 0
instrucCounter = 0
curr = startNodes
visitedZ = set()
zsteps = []
while True:
    direc = instruc[instrucCounter % len(instruc)]
    nextNodes = []
    for elem in curr:
        nextelem  = network[elem][0] if direc == 'L' else network[elem][1]
        nextNodes.append(nextelem)

        if nextelem[-1] == "Z":
            if nextelem not in visitedZ:
                zsteps.append(steps+1)
                visitedZ.add(elem)
                
    curr = nextNodes
    if len(zsteps) == len(curr):
        break


    steps += 1
    instrucCounter += 1

print(zsteps)
print(lcm(*zsteps))
