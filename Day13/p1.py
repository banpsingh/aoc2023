import numpy as np

def horizontal(puzzle):

    for b in range(1, len(puzzle)):
        correct = True
        minRows = min(len(puzzle)-b, b)
        for i in range(minRows):
                if not all(x==y for x,y in zip(puzzle[b-1-i], puzzle[b+i])):
                    correct = False
        if correct:
            return b
    
    return 0
    

with open("input.txt", "r") as file:
    data = file.read().strip().split("\n\n")
data = [i.split("\n") for i in data]
puzzles = [[list(p) for p in y] for y in data]

res = 0
for i in range(len(puzzles)):

    res += horizontal(puzzles[i]) * 100 + horizontal(np.transpose(puzzles[i]))

print(res)