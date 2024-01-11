
def moveNorth():
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == "O":
                i = row
                i -= 1

                while i >= 0:
                    if data[i][col] == '#' or data[i][col] == 'O':
                        break
                    i -= 1

                data[row][col] = '.'
                data[i+1][col] = 'O'

def moveSouth():
    for row in range(len(data)-1,-1,-1):
        for col in range(len(data[0])-1,-1,-1):
            if data[row][col] == "O":
                i = row 
                i += 1

                while i < len(data):
                    if data[i][col] == '#' or data[i][col] == 'O':
                        break
                    i += 1

                data[row][col] = '.'
                data[i-1][col] = 'O'

def moveWest():
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == "O":
                j = col
                j -= 1

                while j >= 0:
                    if data[row][j] == '#' or data[row][j] == 'O':
                        break
                    j -= 1

                data[row][col] = '.'
                data[row][j+1] = 'O'

def moveEast():
    for row in range(len(data)-1,-1,-1):
        for col in range(len(data[0])-1,-1,-1):
            if data[row][col] == "O":
                j = col
                j += 1

                while j < len(data[0]):
                    if data[row][j] == '#' or data[row][j] == 'O':
                        break
                    j += 1

                data[row][col] = '.'
                data[row][j-1] = 'O'


def cycle():
    global cycleCount
    global breakFlag
    global cycleStart
    global cycleEnd

    moveNorth()    
    moveWest()
    moveSouth()
    moveEast()

    if not breakFlag:
        cycleCount += 1

        for i, arr in enumerate(listOfDatas):
            if data == arr:
                breakFlag = True
                cycleStart = i 
                cycleEnd = cycleCount 
        
        listOfDatas.append([row[:] for row in data])


with open("input.txt", "r") as file:
    data = [list(i) for i in file.read().strip().split('\n')]

cycleCount = 0
cycleStart, cycleEnd = 0, 0

listOfDatas = []
listOfDatas.append([row[:] for row in data])

breakFlag = False

for i in range(1000000000):
    cycle()
    if breakFlag:
        break

cycleLen = cycleEnd - cycleStart
for i in range((1000000000-cycleStart) % cycleLen):
    cycle()
   

res = sum([(len(data)-i)*sum([1 for item in data[i] if item=='O']) for i in range(len(data))])

print(res)