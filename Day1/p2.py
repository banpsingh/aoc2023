digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}



def checkWord(word):
    for key in digits:
        if key in word:
            return digits[key]
    return False


with open("input.txt", "r") as file:
    res = 0
    for row in file:
        row.strip()
        word = ""
        digit1, digit2 = None, None
        for char in row:
            if char.isdigit():
                digit1 = int(char)
                break
            else:
                word += char
                val = checkWord(word)
                if val:
                    digit1 = val
                    break
        
        word = ""
        for char in row[::-1]:
            if char.isdigit():
                digit2 = int(char)
                break
            else:
                word += char
                val = checkWord(word[::-1])
                if val:
                    digit2 = val
                    break
            
        res += digit1 * 10 + digit2
       

    print(res)

