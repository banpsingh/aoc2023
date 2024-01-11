
with open("input.txt", "r") as file:
    card = 1
    winMap = {}
    
    for row in file:
        _ , data = row.split(":")
        data.strip()
        winNums, pickNums = data.split("|")

        winNums = winNums.strip().split(" ")
        pickNums = pickNums.strip().split(" ")

        winNums = [x for x in winNums if x != ""] #removes empty character elements due to single digit numbers
        pickNums = [x for x in pickNums if x != ""]

        winNums = [int(x) for x in winNums] 
        pickNums = [int(x) for x in pickNums] 
        winNums = set(winNums)

        matches = 0 

        for val in pickNums:
            if val in winNums:
                matches += 1
        
        
        winMap[card] = matches
        card += 1

    countMap = {i:1 for i in range(1, card)}
    stack = []

    for i in range(1, card):

        if winMap[i] > 0: #if the card has some matching numbers
            for j in range(i+1, i + winMap[i]+1):
                stack.append(j)
        
        while stack:
            num = stack.pop()
            countMap[num] += 1

            if winMap[num] > 0: #if the card has some matching numbers
                for j in range(num+1, num + winMap[num]+1):
                    stack.append(j)


    print(sum(countMap.values()))