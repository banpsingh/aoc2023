
def hash(str):
    curr = 0 
    for char in str:
        curr += ord(char)
        curr *= 17
        curr = curr % 256
    
    return curr

def updateEqual(label, focallen):
    boxIndex = hash(label)
    found = False
    for i,val in enumerate(hashmap[boxIndex]):
        if val[0] == label:
            val[1] = focallen
            found = True
        
    if not found:
        hashmap[boxIndex].append([label, focallen])
    

def updateDash(label):
    boxIndex = hash(label)
    for i,val in enumerate(hashmap[boxIndex]):
        if val[0] == label:
            hashmap[boxIndex].remove(val)



data = []
hashmap = [[] for _ in range(256)] 

with open("input.txt", "r") as file:
    inputdata = file.read().strip().split("\n")
    for row in inputdata:
        x = row.split(",")
        data += x


for instruc in data:
    if "=" in instruc:
        index = instruc.index("=")
        label = instruc[:index]
        focallen = int(instruc[index+1:])
        updateEqual(label, focallen)
    else:
        label = instruc[:-1]
        updateDash(label)

res = 0
for i,box in enumerate(hashmap):
    boxNum = i+1
    for j, val in enumerate(box):
        slotNum = j + 1
        focallen = val[1]
        res += boxNum * slotNum * focallen


print(res)

