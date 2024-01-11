
with open("input.txt", "r") as file:
    data = [list(i) for i in  file.read().split("\n")]

S = None
Snorth = None
Ssouth = None
Seast = None
Swest = None
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'S':
            S = (i, j)
            Snorth = (i-1, j)
            Ssouth = (i+1, j)
            Seast = (i, j+1)
            Swest = (i, j-1)

start = None
if data[Snorth[0]][Snorth[1]] in ["|", "F", "7"]:
    start = (Snorth[0], Snorth[1], data[Snorth[0]][Snorth[1]], "north")
elif data[Ssouth[0]][Ssouth[1]] in ["|", "L", "J"]:
    start = (Ssouth[0], Ssouth[1], data[Ssouth[0]][Ssouth[1]], "south")
elif data[Seast[0]][Seast[1]] in ["-", "J", "7"]:
    start = (Seast[0], Seast[1], data[Seast[0]][Seast[1]], "east")
else:
    start = (Swest[0], Swest[1], data[Swest[0]][Swest[1]], "west")
print(S)
print(start)

#north of S needs to be | F 7 
#south of S needs to be | L J
#east of S needs to - J 7 
#west of S needs to - L F

def step(i, j, char, dir):
    if char == '|':
        return (i+1, j, data[i+1][j], "south") if dir == "south" else (i-1, j, data[i-1][j], "north")
    elif char == '-':
        return (i, j+1, data[i][j+1], "east") if dir == "east" else (i, j-1, data[i][j-1], "west")
    elif char == 'L': 
        return (i, j+1, data[i][j+1], "east") if dir == "south" else (i-1, j, data[i-1][j], "north")
    elif char == 'J':
        return (i, j-1, data[i][j-1], "west") if dir == "south" else (i-1, j, data[i-1][j], "north")
    elif char == '7':
        return (i, j-1, data[i][j-1], "west") if dir == "north" else (i+1, j, data[i+1][j], "south")
    elif char == 'F':
        return (i, j+1, data[i][j+1], "east") if dir == "north" else (i+1, j, data[i+1][j], "south")

curr = start
count = 1
while curr[2] != 'S':
    curr = step(curr[0], curr[1], curr[2], curr[3])
    count += 1

print(count // 2)