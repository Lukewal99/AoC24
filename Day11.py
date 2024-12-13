file = open("PuzzleInput.txt", "r").read()
stones = file.split(" ")
part = 2
sum = 0

#if part == 1:
#    for i in range(0,25):
        #print(stones)
        #print (i)
#        j=0
#        while j in range(0,len(stones)):
#            stone = stones[j]
#            if stone == '0':
#                stones[j] = '1'
#            elif len(stone) % 2 == 0:
#                a = int(len(stone)/2)
#                stones[j] = str(int(stone[0:a]))
#                stones.insert(j+1,str(int(stone[a:len(stone)])))
#                j+=1
#            else:
#                stones[j] = str(int(stone)*2024)
#            j+=1
#    sum = len(stones)

if part == 1:
    x = 25
elif part == 2:
    x = 75

stonesDict = {}
for stone in stones:
    stonesDict[int(stone)] = 1

stonesDictCopy = {}
for i in range(0,x):
    for key in stonesDict.keys():
        if key==0:
            if 1 in stonesDictCopy.keys():
                stonesDictCopy[1] += stonesDict[key]
            else:stonesDictCopy[1] = stonesDict[key]
        
        elif len(str(key))%2 == 0:
            mid=int(len(str(key))/2)
            a = int(str(key)[0:mid])
            b = int(str(key)[mid:len(str(key))])

            if a in stonesDictCopy.keys():
                stonesDictCopy[a] += stonesDict[key]
            else:stonesDictCopy[a] = stonesDict[key]
            if b in stonesDictCopy.keys():
                stonesDictCopy[b] += stonesDict[key]
            else:stonesDictCopy[b] = stonesDict[key]

        else:
            if key*2024 in stonesDictCopy.keys():
                stonesDictCopy[key*2024] += stonesDict[key]
            else:stonesDictCopy[key*2024] = stonesDict[key]

    stonesDict = stonesDictCopy.copy()
    stonesDictCopy = {}
    
for value in stonesDict.values():
    sum+= value

print(sum)