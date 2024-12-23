import time
start = time.time()
map = open("PuzzleInput.txt", "r").read().split("\n")
part = 2

for y in range(0,len(map)):
    line = list(map[y])
    map[y] = line
    if 'S' in line:
        for x in range(0,len(map[y])):
            if map[y][x] == 'S':
                startPos = [y,x]

i = 0
y, x = startPos
path = []
while map[y][x] != 'E':
    map[y][x] = i
    path.insert(i,[y,x])
    if map[y-1][x] == '.' or map[y-1][x] == 'E':
        y-=1
    elif map[y][x+1] == '.' or map[y][x+1] == 'E':
        x+=1
    elif map[y+1][x] == '.' or map[y+1][x] == 'E':
        y+=1
    elif map[y][x-1] == '.' or map[y][x-1] == 'E':
        x-=1
    i+=1
map[y][x] = i
path.insert(i,[y,x])
cheats = {}

if part == 1:
    for i in range(0,len(path)):
        y, x = path[i]
        if y > 1:
            if map[y-1][x] == '#' and map[y-2][x] != '#' and (y-1,x) not in cheats.keys():
                cheats[y-1,x] = (map[y-2][x] - map[y][x]) -2
        if x < len(map[y])-2:
            if map[y][x+1] == '#' and map[y][x+2] != '#' and (y,x+1) not in cheats.keys():
                cheats[y,x+1] = (map[y][x+2] - map[y][x]) -2
        if y < len(map)-2:
            if map[y+1][x] == '#' and map[y+2][x] != '#' and (y+1,x) not in cheats.keys():
                cheats[y+1,x] = (map[y+2][x] - map[y][x]) -2
        if x > 1:
            if map[y][x-1] == '#' and map[y][x-2] != '#' and (y,x-1) not in cheats.keys():
                cheats[y,x-1] = (map[y][x-2] - map[y][x]) -2

elif part == 2:
    for i in range(0,len(path)):
        startY, startX = path[i]
        for y in range(startY-20,startY+21):
            if 0 <= y and y < len(map):
                k = 20-abs(y-startY) 
                for x in range(startX-k,startX+k+1):
                    if 0 <= x and x < len(map[y]):
                        if map[y][x] != '#' and [y,x] != [startY,startX]: 
                                if (startY, startX, y, x) not in cheats.keys() and (y, x, startY, startX) not in cheats.keys():
                                    manhattanDistance = abs(y-startY) + abs(x-startX)
                                    cheats[startY, startX, y, x] = abs(map[y][x] - map[startY][startX]) - manhattanDistance



a = list(cheats.values())
a.sort(reverse=True)
#counts = {}


for i in range(0,len(a)):
    if a[i] < 100:
        print(i)
        break

#for i in range(0,len(a)):
#    if a[i] in counts.keys():
#        counts[a[i]] += 1
#    else:
#        counts[a[i]] = 1
#for key in counts.keys():
#    print(str(key) + ", " + str(counts[key]))

end = time.time()
print(end - start)
