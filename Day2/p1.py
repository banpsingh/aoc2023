
with open("input.txt", "r") as file:
    rowNum = 1
    res = 0
    for row in file:
        possible = True
        row.strip()
        _ , game = row.split(':')
        game = game.split(';')
        game = [i.strip() for i in game]
        game = [i.split(', ') for i in game] 
        #print(game)
        for bag in game:
            data = [i.split() for i in bag]
            #print(data)
            for amt,color in data:
                #print(amt, color)
                if int(amt) > 12 and color == 'red':
                    possible = False
                elif int(amt) > 13 and color == 'green':
                    possible = False
                elif int(amt) > 14:
                    possible = False
        
        if possible:
            res += rowNum
        rowNum += 1
    
    print(res)