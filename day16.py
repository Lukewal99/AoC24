file = open("PuzzleInput.txt", "r").read()
map = file.split("\n")

queue = {}
paths = {}
visited = {}
solutions = []
solPaths = []

for y in range (0,len(map)):
    if 'S' in map[y]:
        for x in range(0,len(map[y])):
            if map[y][x] == 'S':
                queue[x,y,'E'] = 0
                paths[x,y,'E'] = []
                break
        break

while len(queue.keys()) != 0:
    x, y, dir = list(queue.keys())[0]
    visited[x,y,dir] = queue[x,y,dir]
    if map[y][x] == 'E':
        solutions.append(queue[x,y,dir])
        solPaths.append(paths[x,y,dir]+ [[x,y]])
    
    if dir == 'N':
        if map[y-1][x] != '#':
            if (x,y-1,'N') in visited:
                if visited[x,y-1,'N'] > queue[x,y,'N']+1:
                    queue[x,y-1,'N'] = queue[x,y,'N']+1
                    paths[x,y-1,'N'] = paths[x,y,'N'] + [[x,y]]
            else:
                queue[x,y-1,'N'] = queue[x,y,'N']+1
                paths[x,y-1,'N'] = paths[x,y,'N'] + [[x,y]]

        if map[y][x+1] != '#': 
            if (x,y,'E') in visited:
                if visited[x,y,'E'] > queue[x,y,'N']+1000:
                    queue[x,y,'E'] = queue[x,y,'N']+1000
                    paths[x,y,'E'] = paths[x,y,'N']
            else:
                queue[x,y,'E'] = queue[x,y,'N']+1000
                paths[x,y,'E'] = paths[x,y,'N']
    
        if map[y][x-1] != '#': 
            if (x,y,'W') in visited:
                if visited[x,y,'W'] > queue[x,y,'N']+1000:
                    queue[x,y,'W'] = queue[x,y,'N']+1000
                    paths[x,y,'W'] = paths[x,y,'N']
            else:
                queue[x,y,'W'] = queue[x,y,'N']+1000
                paths[x,y,'W'] = paths[x,y,'N']

    elif dir == 'S':
        if map[y+1][x] != '#':
            if (x,y+1,'S') in visited:
                if visited[x,y+1,'S'] > queue[x,y,'S']+1:
                    queue[x,y+1,'S'] = queue[x,y,'S']+1
                    paths[x,y+1,'S'] = paths[x,y,'S'] + [[x,y]]
            else:
                queue[x,y+1,'S'] = queue[x,y,'S']+1
                paths[x,y+1,'S'] = paths[x,y,'S'] + [[x,y]]

        if map[y][x+1] != '#': 
            if (x,y,'E') in visited:
                if visited[x,y,'E'] > queue[x,y,'S']+1000:
                    queue[x,y,'E'] = queue[x,y,'S']+1000
                    paths[x,y,'E'] = paths[x,y,'S']
            else:
                queue[x,y,'E'] = queue[x,y,'S']+1000
                paths[x,y,'E'] = paths[x,y,'S']
    
        if map[y][x-1] != '#': 
            if (x,y,'W') in visited:
                if visited[x,y,'W'] > queue[x,y,'S']+1000:
                    queue[x,y,'W'] = queue[x,y,'S']+1000
                    paths[x,y,'W'] = paths[x,y,'S']
            else:
                queue[x,y,'W'] = queue[x,y,'S']+1000
                paths[x,y,'W'] = paths[x,y,'S']

    elif dir == 'E':
        if map[y][x+1] != '#':
            if (x+1,y,'E') in visited:
                if visited[x+1,y,'E'] > queue[x,y,'E']+1:
                    queue[x+1,y,'E'] = queue[x,y,'E']+1
                    paths[x+1,y,'E'] = paths[x,y,'E'] + [[x,y]]
            else:
                queue[x+1,y,'E'] = queue[x,y,'E']+1
                paths[x+1,y,'E'] = paths[x,y,'E'] + [[x,y]]

        if map[y-1][x] != '#': 
            if (x,y,'N') in visited:
                if visited[x,y,'N'] > queue[x,y,'E']+1000:
                    queue[x,y,'N'] = queue[x,y,'E']+1000
                    paths[x,y,'N'] = paths[x,y,'E']
            else:
                queue[x,y,'N'] = queue[x,y,'E']+1000
                paths[x,y,'N'] = paths[x,y,'E']
    
        if map[y+1][x] != '#': 
            if (x,y,'S') in visited:
                if visited[x,y,'S'] > queue[x,y,'E']+1000:
                    queue[x,y,'S'] = queue[x,y,'E']+1000
                    paths[x,y,'S'] = paths[x,y,'E']
            else:
                queue[x,y,'S'] = queue[x,y,'E']+1000
                paths[x,y,'S'] = paths[x,y,'E']

    elif dir == 'W':
        if map[y][x-1] != '#':
            if (x-1,y,'W') in visited:
                if visited[x-1,y,'W'] > queue[x,y,'W']+1:
                    queue[x-1,y,'W'] = queue[x,y,'W']+1
                    paths[x-1,y,'W'] = paths[x,y,'W'] + [[x,y]]
            else:
                queue[x-1,y,'W'] = queue[x,y,'W']+1
                paths[x-1,y,'W'] = paths[x,y,'W'] + [[x,y]]

        if map[y-1][x] != '#': 
            if (x,y,'N') in visited:
                if visited[x,y,'N'] > queue[x,y,'W']+1000:
                    queue[x,y,'N'] = queue[x,y,'W']+1000
                    paths[x,y,'N'] = paths[x,y,'W']
            else:
                queue[x,y,'N'] = queue[x,y,'W']+1000
                paths[x,y,'N'] = paths[x,y,'W']
    
        if map[y+1][x] != '#': 
            if (x,y,'S') in visited:
                if visited[x,y,'S'] > queue[x,y,'W']+1000:
                    queue[x,y,'S'] = queue[x,y,'W']+1000
                    paths[x,y,'S'] = paths[x,y,'W']
            else:
                queue[x,y,'S'] = queue[x,y,'W']+1000
                paths[x,y,'S'] = paths[x,y,'W']
    queue.pop((x,y,dir))

minSolution = min(solutions)
minSolVisited = []

for i in range(0,len(solutions)):
    if solutions[i] == minSolution:
        print(solPaths[i])
        for item in solPaths[i]:
            if item not in minSolVisited:
                minSolVisited.append(item)

print(minSolution)
print(len(minSolVisited))
# Only getting one solved path