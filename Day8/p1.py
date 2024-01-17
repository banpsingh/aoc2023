with open("input.txt", "r") as file:
    instruc, data = file.read().split("\n\n")

data = data.split("\n")

network = {}
for row in data:
    node, rest = row.split(" = ")
    left, right = rest.split(", ")
    left, right = left[1:], right[:-1]
    network[node] = (left, right)

steps = 0
instrucCounter = 0
curr = 'AAA'
while curr != 'ZZZ':
    direc = instruc[instrucCounter % len(instruc)]
    curr = network[curr][0] if direc == 'L' else network[curr][1]
    steps += 1
    instrucCounter += 1

print(steps)