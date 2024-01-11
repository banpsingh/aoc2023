
def moveRock(i,j):
    orig = i
    newi = i

    i -= 1
    while i >= 0:
        if data[i][j] == '#' or data[i][j] == 'O':
            break
        else:
            newi = i
        i -= 1

    data[orig][j] = '.'
    data[newi][j] = 'O'


with open("input.txt", "r") as file:
    data = [list(i) for i in file.read().strip().split('\n')]

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "O":
            moveRock(i,j)


# res = 0
# for i in range(len(data)):
#     rocksinrow = 0
#     for j in range(len(data[0])):
#         if data[i][j] == "O":
#             rocksinrow += 1
#     res += rocksinrow * (len(data)-i)

res = sum([(len(data)-i)* sum([1 for item in data[i] if item=='O']) for i in range(len(data))])

print(res)