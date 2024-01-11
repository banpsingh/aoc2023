

with open("input.txt", "r") as file:
    res = 0
    for row in file:
        row.strip()
        i=0
        while not row[i].isdigit():
            i += 1
        res += int(row[i])*10

        j = 0 
        while not (row[::-1][j]).isdigit():
            j += 1
        res += int(row[::-1][j])
    

    print(res)