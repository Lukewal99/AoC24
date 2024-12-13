def search(y, x, map, area, perimeter, walls, visited):
    plot = map[y][x]
    visited.append([y,x])
    perimeter += 4
    if [y-0.25,x] not in walls:
        walls.append([y-0.25,x])
    if [y+0.25,x] not in walls:
        walls.append([y+0.25,x])
    if [y,x-0.25] not in walls:
        walls.append([y,x-0.25])
    if [y,x+0.25] not in walls:
        walls.append([y,x+0.25])

    area += 1
    if y >  0:
        if map[y-1][x] == plot:
            perimeter-=1
            if [y-0.25,x]  in walls:
                walls.remove([y-0.25,x])
            if [y-1,x] not in visited:
                area, perimeter, walls, visited = search(y-1, x, map, area, perimeter, walls, visited)

    if x >  0:
        if map[y][x-1] == plot:
            perimeter-=1
            if [y,x-0.25]  in walls:
                walls.remove([y,x-0.25])
            if [y,x-1] not in visited:
                area, perimeter, walls, visited = search(y, x-1, map, area, perimeter, walls, visited)

    if y <  len(map)-1:
        if map[y+1][x] == plot:
            perimeter-=1       
            if [y+0.25,x]  in walls:
                walls.remove([y+0.25,x])
            if [y+1,x] not in visited:
                area, perimeter, walls, visited = search(y+1, x, map, area, perimeter, walls, visited)

    if x <  len(map[y])-1:
        if map[y][x+1] == plot:
            perimeter-=1     
            if [y,x+0.25]  in walls:
                walls.remove([y,x+0.25])
            if [y,x+1] not in visited:
                area, perimeter, walls, visited = search(y, x+1, map, area, perimeter, walls, visited)
    
    return(area, perimeter, walls, visited)


file = open("PuzzleInput.txt", "r").read()
map = file.split("\n")
part = 2
sum = 0

visited = []
regions = []


for y in range(0,len(map)):
    for x in range(0,len(map[y])):
        if [y,x] not in visited:
            area, perimeter, walls, visitedSearch = search(y, x, map, 0, 0, [], [])
            if part == 2:
                numOfWalls = 0
                while len(walls) > 0:
                    wall = walls[0]
                    if int(wall[0]) == wall[0]:
                        # vertical wall
                        numOfWalls+=1
                        X = wall[1]
                        Y = wall [0]
                        while [Y,X] in walls:
                            walls.remove([Y,X])
                            Y-=1
                        Y = wall [0] + 1
                        while [Y,X] in walls:
                            walls.remove([Y,X])
                            Y+=1

                    elif int(wall[1])  == wall[1]:
                        # horizontal wall
                        numOfWalls+=1
                        Y = wall [0]
                        X = wall[1]
                        while [Y,X] in walls:
                            walls.remove([Y,X])
                            X-=1
                        X = wall[1] + 1
                        while [Y,X] in walls:
                            walls.remove([Y,X])
                            X+=1

                    else:
                        print("wtf")
                perimeter = numOfWalls

            regions.append([area,perimeter])
            for plot in visitedSearch:
                visited.append(plot)

for value in regions:
    sum+=value[0]*value[1]
print(sum)
