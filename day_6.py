time, distance = open('txt').read().split('\n')

times=time.split(" ")
times.pop(0)
distances=distance.split(" ")
distances.pop(0)

while "" in distances: distances.remove("")
while "" in times: times.remove("")

totalTime="".join(times)
totalDistance="".join(distances)
print(totalTime)
print(totalDistance)


def waysToWin(time,distance):
    ways=0
    for i in range(time):
        if i*(time-i)>distance:
            ways+=1
    return ways
print(waysToWin(int(totalTime),int(totalDistance)))

possibleWays=[]
for i in range(len(distances)):
    possibleWays.append( waysToWin(int(times[i]),int(distances[i])))
sum=1
for each in possibleWays:
    sum=sum*each

