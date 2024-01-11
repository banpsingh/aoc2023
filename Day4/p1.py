
with open("input.txt", "r") as file:
    res = 0
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
        
        if matches:
            res += 2 ** (matches - 1)

    print(res)