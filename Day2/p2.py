
with open("input.txt", "r") as file:
    res = 0
    for row in file:
        minColors = {'red': 0, 'blue': 0, 'green': 0}
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
                if int(amt) > minColors[color]:
                    minColors[color] = int(amt)
        
        #print(minColors)
        power = 1
        for key in minColors:
            power *= minColors[key]
        res += power
    
    print(res)