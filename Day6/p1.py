
with open("input.txt", "r") as file:
    time, distance = file.read().strip().split("\n")
    
time = time.split(":")[1].strip().split(" ")
time = [int(x) for x in time if x != "" ]

distance = distance.split(":")[1].strip().split(" ")
distance = [int(x) for x in distance if x != ""]

res = 1

for i in range(len(time)):
    recordBreak = 0
    for j in range(time[i]+1):
        timeCharge = j
        timeTravel = time[i] - j 
        speed = timeCharge
        distTravel = speed * timeTravel
        if distTravel > distance[i]:
            recordBreak += 1
    
    res *= recordBreak

print(res)