import math

with open("input.txt", "r") as file:
    data = file.read().strip().split("\n\n")
 
seeds = data[0].split(':')[1].strip().split()
seeds = [int(x) for x in seeds]

def createMapping(num):
    mapping = data[num].split(":")[1].split("\n")[1:]
    mapping = [i.split() for i in mapping]
    mapping = [[int(i) for i in nested] for nested in mapping]
    return mapping

# seedToSoil = createMapping(1)
# soilToFert = createMapping(2)
# fertToWater = createMapping(3)
# waterToLight = createMapping(4)
# lightToTemp = createMapping(5)
# tempToHum = createMapping(6)
# humToLoc = createMapping(7)

listOfMappings = [createMapping(i) for i in range(1,8)]

def forwardMap(curr, mapping):
    for dest, source, rge in mapping:
        if curr >= source and curr <= source + rge:
            diff = curr - source
            curr = dest + diff
            break
    return curr

res = math.inf
for i in seeds:
    curr = i
    for mapping in listOfMappings:
        curr = forwardMap(curr,mapping) 
    res = min(res, curr)

print(res)