from tqdm import trange
import math

with open("input.txt", "r") as file:
    data = file.read().strip().split("\n\n")
    seeds = data[0].split(':')[1].strip().split()
    seeds = [int(x) for x in seeds]
    seeds = [(seeds[i],seeds[i+1]) for i in range(0, len(seeds), 2)]

    seedToSoil = data[1].split(":")[1].split("\n")[1:]
    seedToSoil = [i.split() for i in seedToSoil]
    seedToSoil = [[int(i) for i in nested] for nested in seedToSoil]

    soilToFert = data[2].split(":")[1].split("\n")[1:]
    soilToFert = [i.split() for i in soilToFert]
    soilToFert = [[int(i) for i in nested] for nested in soilToFert]

    fertToWater = data[3].split(":")[1].split("\n")[1:]
    fertToWater = [i.split() for i in fertToWater]
    fertToWater = [[int(i) for i in nested] for nested in fertToWater]

    waterToLight = data[4].split(":")[1].split("\n")[1:]
    waterToLight = [i.split() for i in waterToLight]
    waterToLight = [[int(i) for i in nested] for nested in waterToLight]

    lightToTemp = data[5].split(":")[1].split("\n")[1:]
    lightToTemp = [i.split() for i in lightToTemp]
    lightToTemp = [[int(i) for i in nested] for nested in lightToTemp]

    tempToHum = data[6].split(":")[1].split("\n")[1:]
    tempToHum = [i.split() for i in tempToHum]
    tempToHum = [[int(i) for i in nested] for nested in tempToHum]

    humToLoc = data[7].split(":")[1].split("\n")[1:]
    humToLoc = [i.split() for i in humToLoc]
    humToLoc = [[int(i) for i in nested] for nested in humToLoc]

    res = math.inf
    for start, length in seeds:
        for i in trange(start, start+length):
            curr = i 
            for dest, source, rge in seedToSoil:
                if curr >= source and curr <= source + rge:
                    diff = curr - source
                    curr = dest + diff
                    break
            for dest, source, rge in soilToFert:
                if curr >= source and curr <= source + rge:
                    diff = curr - source
                    curr = dest + diff
                    break
            for dest, source, rge in fertToWater:
                if curr >= source and curr <= source + rge:
                    diff = curr - source
                    curr = dest + diff
                    break
            for dest, source, rge in waterToLight:
                if curr >= source and curr <= source + rge:
                    diff = curr - source
                    curr = dest + diff
                    break
            for dest, source, rge in lightToTemp:
                if curr >= source and curr <= source + rge:
                    diff = curr - source
                    curr = dest + diff
                    break
            for dest, source, rge in tempToHum:
                if curr >= source and curr <= source + rge:
                    diff = curr - source
                    curr = dest + diff
                    break
            for dest, source, rge in humToLoc:
                if curr >= source and curr <= source + rge:
                    diff = curr - source
                    curr = dest + diff
                    break
            
            res = min(res, curr)
    
    print(res)