from tqdm import trange 

with open("sample.txt", "r") as file:
    time, distance = file.read().strip().split("\n")
    
time = time.split(":")[1].strip().split(" ")

timeStr = ''
for i in time:
    if i != "":
        timeStr += i

time = int(timeStr)


distance = distance.split(":")[1].strip().split(" ")

distStr = ''
for i in distance:
    if i != "":
        distStr += i

distance = int(distStr)

res = 0

for i in trange(time+1):
    timeCharge = i
    timeTravel = time - i 
    speed = timeCharge
    distTravel = speed * timeTravel
    if distTravel > distance:
        res += 1


print(res)