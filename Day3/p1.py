
def isPartNumber(data, i, jStart, jEnd):
    res = False
    rowAbove = (i-1) >= 0
    rowBelow = (i + 1) < len(data)
    colLeft = (jStart - 1) >= 0
    colRight = (jEnd + 1) < len(data[0])

    if colLeft and colRight:
        if rowAbove and rowBelow:
            for idx in range(jStart-1, jEnd+2):
                charAbove = data[i-1][idx]
                isDigit = charAbove.isdigit()
                if charAbove != '.' and not isDigit:
                    res = True
                
                charBelow = data[i+1][idx]
                isDigit = charBelow.isdigit()
                if charBelow != '.' and not isDigit:
                    res = True

            charLeft = data[i][jStart-1]
            isDigit = charLeft.isdigit()
            if charLeft != '.' and not isDigit:
                res = True
            
            charRight = data[i][jEnd+1]
            isDigit = charRight.isdigit()
            if charRight != '.' and not isDigit:
                res = True

        elif rowAbove:
            for idx in range(jStart-1, jEnd+2):
                charAbove = data[i-1][idx]
                isDigit = charAbove.isdigit()
                if charAbove != '.' and not isDigit:
                    res = True

            charLeft = data[i][jStart-1]
            isDigit = charLeft.isdigit()
            if charLeft != '.' and not isDigit:
                res = True
            
            charRight = data[i][jEnd+1]
            isDigit = charRight.isdigit()
            if charRight != '.' and not isDigit:
                res = True

        elif rowBelow:
            for idx in range(jStart-1, jEnd+2):
                charBelow = data[i+1][idx]
                isDigit = charBelow.isdigit()
                if charBelow != '.' and not isDigit:
                    res = True

            charLeft = data[i][jStart-1]
            isDigit = charLeft.isdigit()
            if charLeft != '.' and not isDigit:
                res = True
            
            charRight = data[i][jEnd+1]
            isDigit = charRight.isdigit()
            if charRight != '.' and not isDigit:
                res = True
    elif colLeft:
        if rowAbove and rowBelow:
            for idx in range(jStart-1, jEnd+1):
                charAbove = data[i-1][idx]
                isDigit = charAbove.isdigit()
                if charAbove != '.' and not isDigit:
                    res = True
                
                charBelow = data[i+1][idx]
                isDigit = charBelow.isdigit()
                if charBelow != '.' and not isDigit:
                    res = True

            charLeft = data[i][jStart-1]
            isDigit = charLeft.isdigit()
            if charLeft != '.' and not isDigit:
                res = True
            

        elif rowAbove:
            for idx in range(jStart-1, jEnd+1):
                charAbove = data[i-1][idx]
                isDigit = charAbove.isdigit()
                if charAbove != '.' and not isDigit:
                    res = True

            charLeft = data[i][jStart-1]
            isDigit = charLeft.isdigit()
            if charLeft != '.' and not isDigit:
                res = True

        elif rowBelow:
            for idx in range(jStart-1, jEnd+1):
                charBelow = data[i+1][idx]
                isDigit = charBelow.isdigit()
                if charBelow != '.' and not isDigit:
                    res = True

            charLeft = data[i][jStart-1]
            isDigit = charLeft.isdigit()
            if charLeft != '.' and not isDigit:
                res = True

    elif colRight:
        if rowAbove and rowBelow:
            for idx in range(jStart, jEnd+2):
                charAbove = data[i-1][idx]
                isDigit = charAbove.isdigit()
                if charAbove != '.' and not isDigit:
                    res = True
                
                charBelow = data[i+1][idx]
                isDigit = charBelow.isdigit()
                if charBelow != '.' and not isDigit:
                    res = True
            
            charRight = data[i][jEnd+1]
            isDigit = charRight.isdigit()
            if charRight != '.' and not isDigit:
                res = True

        elif rowAbove:
            for idx in range(jStart, jEnd+2):
                charAbove = data[i-1][idx]
                isDigit = charAbove.isdigit()
                if charAbove != '.' and not isDigit:
                    res = True
            
            charRight = data[i][jEnd+1]
            isDigit = charRight.isdigit()
            if charRight != '.' and not isDigit:
                res = True

        elif rowBelow:
            for idx in range(jStart, jEnd+2):
                charBelow = data[i+1][idx]
                isDigit = charBelow.isdigit()
                if charBelow != '.' and not isDigit:
                    res = True
            
            charRight = data[i][jEnd+1]
            isDigit = charRight.isdigit()
            if charRight != '.' and not isDigit:
                res = True

    return res

with open("input.txt", "r") as file:
    fileStr = file.read()
    fileStr = fileStr.strip()
    data = fileStr.split("\n")
    data = [list(i) for i in data]
    
    res = 0

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
                if isPartNumber(data, i, start[1], end[1]):
                    val = int("".join(data[i][start[1]:end[1]+1]))
                    print(val)
                    res += val

            # print(data[i][j])
            j += 1
        i += 1
    print("-------------")
    print(res)