
with open("input.txt", "r") as file:
    data = [i.split(" ") for i in file.read().strip().split("\n")]


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
    elif spring[i] == "?":
        return combo(spring[:i]+'.'+spring[i+1:],code,i+1) + combo(spring[:i]+'#'+spring[i+1:],code,i+1)
    else:
        return combo(spring,code,i+1)

res = 0

count = 1
for spring, code in data:
    code = code.split(",")

    
    res += combo(spring,code,0)
    
print(res)