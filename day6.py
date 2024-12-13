def column(matrix, i):
    return [row[i] for row in matrix]

file = open("PuzzleInput.txt", "r").read()
part = 2
sum = 1
debug = False

map = file.split("\n")
guardX = 0
guardY = 0
guardDir = 'N'
#find guard
for y in range(0,len(map)):
    if '^' in map[y]:
        guardY = y
        guardX = map[y].find('^')

n = []
e = []
s = []
w = []

map[guardY] = map[guardY][0:guardX] + 'X' + map[guardY][guardX+1:len(map[guardY])]
while guardY >= 0 and guardX >= 0 and guardY < len(map) and guardX < len(map[0]):
    if guardDir == 'N':
        if guardY > 0:
            if map[guardY-1][guardX] == '#':
                n.append([guardY-1,guardX])
                guardDir = 'E'
            else:
                guardY-=1
                if map[guardY][guardX] != 'X':
                    map[guardY] = map[guardY][0:guardX] + 'X' + map[guardY][guardX+1:len(map[guardY])]
                    sum+=1
        else:
            break

    elif guardDir == 'E':
        if guardX < len(map[0])-1:
            if map[guardY][guardX+1] == '#':
                e.append([guardY,guardX+1])
                guardDir = 'S'
            else:
                guardX+=1
                if map[guardY][guardX] != 'X':
                    map[guardY] = map[guardY][0:guardX] + 'X' + map[guardY][guardX+1:len(map[guardY])]
                    sum+=1
        else:
            break

    elif guardDir == 'S':
        if guardY < len(map)-1:
            if map[guardY+1][guardX] == '#':
                s.append([guardY+1,guardX])
                guardDir = 'W'
            else:
                guardY+=1
                if map[guardY][guardX] != 'X':
                    map[guardY] = map[guardY][0:guardX] + 'X' + map[guardY][guardX+1:len(map[guardY])]
                    sum+=1
        else:
            break
    elif guardDir == 'W':
        if guardX > 0:
            if map[guardY][guardX-1] == '#':
                w.append([guardY,guardX-1])
                guardDir = 'N'
            else:
                guardX-=1
                if map[guardY][guardX] != 'X':
                    map[guardY] = map[guardY][0:guardX] + 'X' + map[guardY][guardX+1:len(map[guardY])]
                    sum+=1
        else:
            break


paradoxSum = 0
if part == 2:
    for item in n:
        map[item[0]] = map[item[0]][0:item[1]] + "V" +  map[item[0]][item[1]+1:len(map[0])]
    for item in e:
        map[item[0]] = map[item[0]][0:item[1]] + "<" +  map[item[0]][item[1]+1:len(map[0])]
    for item in s:
        map[item[0]] = map[item[0]][0:item[1]] + "^" +  map[item[0]][item[1]+1:len(map[0])]
    for item in w:
        map[item[0]] = map[item[0]][0:item[1]] + ">" +  map[item[0]][item[1]+1:len(map[0])]

    # Doesnt work. Just brute force replaing every block instead

    # for y in range(0,len(map)):
    #     row = map[y]
    #     if 'V' in row:
    #         for x in range(0,len(map[0])):
    #             if map[y][x] == 'V':

    #                 rowTwo = map[y+1]
    #                 if '<' in rowTwo:
    #                     for xTwo in range(x,len(map[0])):
    #                         if rowTwo[xTwo] == '<':

    #                             colThree = column(map,xTwo-1)
    #                             if '^' in colThree:
    #                                 #add a > to loop
    #                                 paradoxSum+=1
    #                                 break
    #                     break
            
        
    #     if '<' in row:
    #         for x in range(0,len(map[0])):
    #             if map[y][x] == '<':

    #                 col = column(map,x-1)
    #                 if '^' in col:
    #                     for yTwo in range(y,len(map)):
    #                         if map[yTwo][x-1] == '^':

    #                             rowTwo = map[yTwo-1]
    #                             if '>' in rowTwo:
    #                                 # add a V to loop
    #                                 paradoxSum+=1
    #                                 break
    #                     break
            
        
    #     if '^' in row:
    #         for x in range(0,len(map[0])):
    #             if map[y][x] == '^':

    #                 rowTwo = map[y-1]
    #                 if '>' in rowTwo:
    #                     for xTwo in range(x,0,-1):
    #                         if rowTwo[xTwo] == '>':

    #                             colThree = column(map,xTwo+1)
    #                             if 'V' in colThree:
    #                                 #add a < to loop
    #                                 paradoxSum+=1
    #                                 break
    #                     break
            

    #     if '>' in row:
    #         for x in range(0,len(map[0])):
    #             if map[y][x] == '>':

    #                 col = column(map,x+1)
    #                 if 'V' in col:
    #                     for yTwo in range(y,0,-1):
    #                         if map[yTwo][x+1] == 'V':

    #                             rowTwo = map[yTwo+1]
    #                             if '<' in rowTwo:
    #                                 # add a ^ to loop
    #                                 paradoxSum+=1
    #                                 break
    #                     break
            



if debug:
    for row in map:
       print(row)
print(sum)

if part==2:
    print(paradoxSum)