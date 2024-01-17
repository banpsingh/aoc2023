
with open("input.txt", "r") as file:
    data = [i.split(" ") for i in file.read().strip().split("\n")]

def isPossible(spring,code):
    orig = spring
    spring = spring.split(".")
    spring = [i for i in spring if i != '']

    for i,group in enumerate(spring):
        if '?' in group:
            return True
        elif len(group) != int(code[i]):
            return False
    return True

def isValid(spring, code):
    spring = spring.split(".")
    spring = [i for i in spring if i != '']

    if len(spring) != len(code):
        return False
    for i, group in enumerate(spring):
        if len(group) != int(code[i]):
            return False
    
    return True


def combo(spring,code,i):
    if i == len(spring)-1:
        if spring[i] == '?':
            return combo(spring[:i]+'.',code,i) + combo(spring[:i]+'#',code,i)
        return 1 if isValid(spring,code) else 0
    if not isPossible(spring,code):
        return 0
    if spring[i] == "?":
        return combo(spring[:i]+'.'+spring[i+1:],code,i+1) + combo(spring[:i]+'#'+spring[i+1:],code,i+1)
    else:
        return combo(spring,code,i+1)

res = 0
comboList = []
count = 1
for spring, code in data:
    orig = spring
    for _ in range(4):
        spring += '?' + orig
        
    code = code.split(",")
    code *= 5


    
    val = combo(spring,code,0)
    comboList.append(val)
    res += val
  
print(res)