import math

def isPartNumber(data, i, jStart, jEnd, gearMap):

    val = int("".join(data[i][start[1]:end[1]+1]))

    rowAbove = (i-1) >= 0
    rowBelow = (i + 1) < len(data)
    colLeft = (jStart - 1) >= 0
    colRight = (jEnd + 1) < len(data[0])

    if colLeft and colRight:
        if rowAbove and rowBelow:
            for idx in range(jStart-1, jEnd+2):
                charAbove = data[i-1][idx]
                if charAbove == '*':
                    gearMap[(i-1,idx)].append(val)
                
                charBelow = data[i+1][idx]
                if charBelow == '*':
                    gearMap[(i+1,idx)].append(val)

            charLeft = data[i][jStart-1]
            if charLeft == '*':
                gearMap[(i,jStart-1)].append(val)
            
            charRight = data[i][jEnd+1]
            if charRight == '*':
                gearMap[(i,jEnd+1)].append(val)

        elif rowAbove:
            for idx in range(jStart-1, jEnd+2):
                charAbove = data[i-1][idx]
                if charAbove == '*':
                    gearMap[(i-1,idx)].append(val)

            charLeft = data[i][jStart-1]
            if charLeft == '*':
                gearMap[(i,jStart-1)].append(val)
            
            charRight = data[i][jEnd+1]
            if charRight == '*':
                gearMap[(i,jEnd+1)].append(val)

        elif rowBelow:
            for idx in range(jStart-1, jEnd+2):
                charBelow = data[i+1][idx]
                if charBelow == '*':
                    gearMap[(i+1,idx)].append(val)

            charLeft = data[i][jStart-1]
            if charLeft == '*':
                gearMap[(i,jStart-1)].append(val)
            
            charRight = data[i][jEnd+1]
            if charRight == '*':
                gearMap[(i,jEnd+1)].append(val)

    elif colLeft:
        if rowAbove and rowBelow:
            for idx in range(jStart-1, jEnd+1):
                charAbove = data[i-1][idx]
                if charAbove == '*':
                    gearMap[(i-1,idx)].append(val)
                
                charBelow = data[i+1][idx]
                if charBelow == '*':
                    gearMap[(i+1,idx)].append(val)

            charLeft = data[i][jStart-1]
            if charLeft == '*':
                gearMap[(i,jStart-1)].append(val)
            

        elif rowAbove:
            for idx in range(jStart-1, jEnd+1):
                charAbove = data[i-1][idx]
                if charAbove == '*':
                    gearMap[(i-1,idx)].append(val)

            charLeft = data[i][jStart-1]
            if charLeft == '*':
                gearMap[(i,jStart-1)].append(val)

        elif rowBelow:
            for idx in range(jStart-1, jEnd+1):
                charBelow = data[i+1][idx]
                if charBelow == '*':
                    gearMap[(i+1,idx)].append(val)

            charLeft = data[i][jStart-1]
            if charLeft == '*':
                gearMap[(i,jStart-1)].append(val)

    elif colRight:
        if rowAbove and rowBelow:
            for idx in range(jStart, jEnd+2):
                charAbove = data[i-1][idx]
                if charAbove == '*':
                    gearMap[(i-1,idx)].append(val)
                
                charBelow = data[i+1][idx]
                if charBelow == '*':
                    gearMap[(i+1,idx)].append(val)
            
            charRight = data[i][jEnd+1]
            if charRight == '*':
                gearMap[(i,jEnd+1)].append(val)

        elif rowAbove:
            for idx in range(jStart, jEnd+2):
                charAbove = data[i-1][idx]
                if charAbove == '*':
                    gearMap[(i-1,idx)].append(val)
            
            charRight = data[i][jEnd+1]
            if charRight == '*':
                gearMap[(i,jEnd+1)].append(val)

        elif rowBelow:
            for idx in range(jStart, jEnd+2):
                charBelow = data[i+1][idx]
                if charBelow == '*':
                    gearMap[(i+1,idx)].append(val)
            
            charRight = data[i][jEnd+1]
            if charRight == '*':
                gearMap[(i,jEnd+1)].append(val)

with open("input.txt", "r") as file:
    fileStr = file.read()
    fileStr = fileStr.strip()
    data = fileStr.split("\n")
    data = [list(i) for i in data]
    
    gearMap = {(i,j):[] for i in range(len(data)) for j in range(len(data[0]))}

    i = 0 
    while i < len(data):
        j = 0 
        while j < len(data[0]):
            char = data[i][j]
            if char.isdigit():
                start = (i,j)
                while (j < len(data[0])) and (data[i][j]).isdigit():
                    j += 1
                end = (i, j-1)
                isPartNumber(data, i, start[1], end[1], gearMap)

        i += 1
    #print(gearMap)
    #print("-------------")

    gearRatioSum = 0

    for key in gearMap:
        if len(gearMap[key]) == 2:
            gearRatio = math.prod(gearMap[key])
            gearRatioSum += gearRatio
    

    print(gearRatioSum)