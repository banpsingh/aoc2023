from functools import cmp_to_key

with open("input.txt", "r") as file:
    cards = []
    for row in file:
        hand, bid = row.split(" ")
        bid = int(bid)
        cards.append((hand,bid))

conversion = {str(i):i for i in range(2, 10)}
conversion['T'] = 10
conversion['J'] = 1
conversion['Q'] = 12
conversion['K'] = 13
conversion['A'] = 14

#Five - 7
#Four - 6
#Full House - 5
#Three - 4
#Two Pair - 3
#One Pair - 2
#High Cards - 1
def identifyHand(hand):
    countMap = {}
    for char in hand:
        countMap[char] = 1 + countMap.get(char, 0)
    
    if 'J' in countMap and countMap['J'] == 5:
        return 7
    elif 'J' in countMap:
        high = None
        for i in hand:
            if i != 'J':
                high = i if high == None or countMap[i] >= countMap[high] else high 
        countMap[high] += countMap['J']
        del countMap['J']

    if len(countMap) == 1:
        return 7
    elif len(countMap) == 2:
        if 4 in countMap.values():
            return 6
        else:
            return 5
    elif len(countMap) == 3:
        if 3 in countMap.values():
            return 4
        else:
            return 3
    elif len(countMap) == 4:
        return 2
    else:
        return 1


def compare(item1, item2):
    hand1, hand2 = item1[0], item2[0]
    val1 = identifyHand(hand1)
    val2 = identifyHand(hand2)
    if val1 != val2:
        return val1 - val2
    else:
        i = 0
        while hand1[i] == hand2[i]:
            i += 1
        return conversion[hand1[i]] - conversion[hand2[i]]
    
    return 0 

cards.sort(key=cmp_to_key(compare))

res = 0
for i, (hand, bid) in enumerate(cards):
    rank = i+1
    res += bid * rank


print(res)