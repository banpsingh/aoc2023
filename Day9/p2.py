
with open("input.txt", "r") as file:
    data = []
    for row in file:
        data.append([int(i) for i in row.strip().split(" ")])


def future(history):
    predictions = []
    predictions.append(history)
    curr = history
    while any(curr):
        diff = []
        for i in range(len(curr)- 1):
            diff.append(curr[i+1]- curr[i])
        curr = diff
        predictions.append(diff)

    for  i in range(1,len(predictions)+1):
        row = predictions[-i]
        if not any(row):
            row.insert(0, 0)
        else:
            row.insert(0, row[0]-predictions[-i+1][0])

    return predictions[0][0]
            

res = 0
for history in data:
    nextVal = future(history)
    res += nextVal
print(res)
