

def hash(str):
    curr = 0 
    for char in str:
        curr += ord(char)
        curr *= 17
        curr = curr % 256
    
    return curr


data = []
with open("input.txt", "r") as file:
    inputdata = file.read().strip().split("\n")
    for row in inputdata:
        x = row.split(",")
        data += x


res = sum([hash(i) for i in data])

print(res)
