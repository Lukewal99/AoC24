file = open("PuzzleInput.txt", "r").read()
mapT , directionsT = file.split("\n\n")
map = mapT.split("\n")
directions = directionsT.replace("\n","")
part = 2
robotPos = []
sum = 0

if part == 2:
    for y in range(0,len(map)):
        line = list(map[y])
        width = len(line)
        for x in range(0,width):
            if(line[2*x] == '.' or line[2*x] == '@'):
                line.insert(2*x+1,'.')
            elif(line[2*x] == '#'):
                line.insert(2*x+1,'#')
            elif(line[2*x] == 'O'):
                line[2*x] = '['
                line.insert(2*x+1,']')
        map[y] = str(line)

for y in range(0,len(map)):
    line = map[y]
    if '@' in line:
        for x in range(0,len(line)):
            if line[x] == '@':
                robotPos = [y,x]
                break
        break

for direction in directions:
    y = robotPos[0]
    x = robotPos[1]

    if part == 1:
        if direction == '<':
            while map[y][x-1] == 'O':
                x-=1
            if map[y][x-1] == '.':
                map[y] = map[y][0:x-1] + 'O' + map[y][x:len(map[y])]
                map[y] = map[y][0:robotPos[1]-1] + '@.' + map[y][robotPos[1]+1:len(map[y])]
                robotPos[1] = robotPos[1] -1

        elif direction == '^':
            while map[y-1][x] == 'O':
                y-=1
            if map[y-1][x] == '.':
                map[y-1] = map[y-1][0:x] + 'O' + map[y-1][x+1:len(map[y-1])]
                map[robotPos[0]-1] = map[robotPos[0]-1][0:x] + '@' + map[robotPos[0]-1][x+1:len(map[robotPos[0]-1])]
                map[robotPos[0]] = map[robotPos[0]][0:x] + '.' + map[robotPos[0]][x+1:len(map[robotPos[0]])]
                robotPos[0] = robotPos[0] -1

        elif direction == '>':
            while map[y][x+1] == 'O':
                x+=1
            if map[y][x+1] == '.':
                map[y] = map[y][0:x+1] + 'O' + map[y][x+2:len(map[y])]
                map[y] = map[y][0:robotPos[1]] + '.@' + map[y][robotPos[1]+2:len(map[y])]
                robotPos[1] = robotPos[1] +1
                
        elif direction == 'v':
            while map[y+1][x] == 'O':
                y+=1
            if map[y+1][x] == '.':
                map[y+1] = map[y+1][0:x] + 'O' + map[y+1][x+1:len(map[y+1])]
                map[robotPos[0]+1] = map[robotPos[0]+1][0:x] + '@' + map[robotPos[0]+1][x+1:len(map[robotPos[0]+1])]
                map[robotPos[0]] = map[robotPos[0]][0:x] + '.' + map[robotPos[0]][x+1:len(map[robotPos[0]])]
                robotPos[0] = robotPos[0] +1

        else:
            print("tf")

    elif part == 2:
        boxes = 0
        xRequired = []
        if direction == '<':
            while map[y][x-1] == ']':
                x-=2
                boxes+=1
            if map[y][x-1] == '.':
                map[y] = map[y][0:x-1] + '[]'*boxes + '@.' + map[y][robotPos[1]+1:len(map[y])]
                robotPos[1] = robotPos[1] -1

        elif direction == '^':
            while map[y-1][x] == '[' or map[y-1][x] == ']':
                y-=1
                #finish this


        elif direction == '>':
            while map[y][x+1] == '[':
                x+=2
                boxes+=1
            if map[y][x+1] == '.':
                map[y] = map[y][0:robotPos[1]] + '.@' + '[]'*boxes + map[y][x+2:len(map[y])] 
                robotPos[1] = robotPos[1] +1
                
        elif direction == 'v':
            #copy ^
            print()

        else:
            print("tf")


for y in range(0,len(map)):
    line = map[y]
    if 'O' in line:
        for x in range(0,len(line)):
            if line[x] == 'O':
                sum+= 100*y+x
                
print(sum)