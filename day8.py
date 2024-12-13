file = open("PuzzleInput.txt", "r").read()
map = file.split("\n")
part = 2

antennas = {}

for y in range(0,len(map)):
    for x in range(0,len(map[y])):
        character = map[y][x]
        if character != '.':
            if character in antennas.keys():
                antennas[character].append([y,x])
            else:
                antennas[character] = [[y,x]]
        

antinodes = []

for antennasOfSameType in antennas.values():
    for a in range(0,len(antennasOfSameType)-1):
        for i in range(a+1,len(antennasOfSameType)):
            antA = antennasOfSameType[a]
            antB = antennasOfSameType[i]
            deltaY = antA[0] - antB[0]
            deltaX = antA[1] - antB[1]

            antinodeAY = antA[0]
            antinodeBY = antB[0]
            antinodeAX = antA[1]
            antinodeBX = antB[1]

            while (antinodeAX >= 0 and antinodeAX <= len(map[0])-1 and antinodeAY >= 0 and antinodeAY <= len(map)-1):
                if  [antinodeAY,antinodeAX] not in antinodes:
                    antinodes.append([antinodeAY,antinodeAX])
                if part == 1:
                    break
                elif part == 2:
                    antinodeAX += deltaX
                    antinodeAY += deltaY

            while (antinodeBX >= 0 and antinodeBX <= len(map[0])-1 and antinodeBY >= 0 and antinodeBY <= len(map)-1):
                if [antinodeBY,antinodeBX] not in antinodes:
                    antinodes.append([antinodeBY,antinodeBX])
                if part == 1:
                    break
                elif part == 2:
                    antinodeBX -= deltaX
                    antinodeBY -= deltaY
            

print(len(antinodes))
#for antinode in antinodes:
#    map[antinode[0]] = map[antinode[0]][0:antinode[1]] + '#' + map[antinode[0]][antinode[1]+1:len(map[antinode[0]])]
#print(map)