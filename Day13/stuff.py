import numpy as np


def horizontal(puzzle):
    for row in puzzle:
        print(row)
    t,b = 0, len(puzzle)-1
    equal = False
    # found = False
    while b > t: 
        #print(b,t)
        if all(x==y for x,y in zip(puzzle[t], puzzle[b])):
            b -= 1
            t += 1
            equal = True
            # found = True 
            # if found:
            #     equal = True
            #equal = found and equal
        else:
            b -=1
            equal = False
            # found = False
    if equal:
        correct = True
        # if b==t:
        #     minRows = min(len(puzzle)-(b+1) ,b) 
        #     for i in range(minRows):
        #         if not all(x==y for x,y in zip(puzzle[b-i], puzzle[b+2+i])):
        #             correct = False
        if b == t:
            correct = False
        if b < t:
            minRows = min(len(puzzle)-(b+1), b+1)
            for i in range(minRows):
                if not all(x==y for x,y in zip(puzzle[b-i], puzzle[b+1+i])):
                    correct = False


        if correct and (b < t):
            return b+1
    

    equal = False
    # found = False
    t,b = 0, len(puzzle)-1
    #print('----')
    while b > t:
        #print(b,t)
        if all(x==y for x,y in zip(puzzle[t], puzzle[b])):
            b -= 1
            t += 1
            equal = True
            # found = True 
            # if found:
            #     equal = True
        else:
            t += 1
            equal = False
            # found = False

    #print(b)
    if equal:
        # print(b,t)
        correct = True
        
        # if b==t:
        #     minRows = min(len(puzzle)-(b+1) ,b) 
        #     for i in range(minRows):
        #         if not all(x==y for x,y in zip(puzzle[b-i], puzzle[b+2+i])):
        #             correct = False
        if b == t:
            correct = False
        if b < t:
            # print(f'b is {b}')
            minRows = min(len(puzzle)-(b+1), b+1)
            # print(f'len of puzzle is {len(puzzle)}')
            # print("minRows is", minRows)
            for i in range(minRows):
                # print("i is",i)
                if not all(x==y for x,y in zip(puzzle[b-i], puzzle[b+1+i])):
                    correct = False

        if correct and (b < t):
            return b + 1
    return 0



with open("input.txt", "r") as file:
    data = file.read().strip().split("\n\n")
data = [i.split("\n") for i in data]
puzzles = [[list(p) for p in y] for y in data]
#print(len(puzzles))

res = 0
for i in range(len(puzzles)):

    res += horizontal(puzzles[i]) * 100 + horizontal(np.transpose(puzzles[i]))


# for i,puzzle in enumerate(puzzles):
    # print(i+1)
    # print(f"index is {i+1}")
    # for row in puzzle:
    #     print(row)
    # print(horizontal(puzzle))
    # for row in np.transpose(puzzle):
    #     print(row)
    # print(horizontal(np.transpose(puzzle)))
    # print('---')
    


for row in puzzles[76]:
    print(row)
print('---------------------------------------------------')
#print(f"horizontal should be 0 and we get {horizontal(puzzles[76])}")
print(f"vertical should be 9 and we get {horizontal(np.transpose(puzzles[76]))}")


print(f"res is {res}")