def search(x,y,corrupted,shortestPath, queue):
    if x < 70 and [x+1,y] not in corrupted:
        if (x+1,y) in shortestPath.keys():
            if len(shortestPath[x+1,y]) > len(shortestPath[x,y])+1:
                shortestPath[x+1,y] = shortestPath[x,y] + [[x,y]]
                queue.append([x+1,y])
        else:
            shortestPath[x+1,y] = shortestPath[x,y] + [[x,y]]
            queue.append([x+1,y])

    if y < 70 and [x,y+1] not in corrupted:
        if (x,y+1) in shortestPath.keys():
            if len(shortestPath[x,y+1]) > len(shortestPath[x,y])+1:
                shortestPath[x,y+1] = shortestPath[x,y] + [[x,y]]
                queue.append([x,y+1])
        else:
            shortestPath[x,y+1] = shortestPath[x,y] + [[x,y]]
            queue.append([x,y+1])

    if x > 0 and [x-1,y] not in corrupted:
        if (x-1,y) in shortestPath.keys():
            if len(shortestPath[x-1,y]) > len(shortestPath[x,y])+1:
                shortestPath[x-1,y] = shortestPath[x,y] + [[x,y]]
                queue.append([x-1,y])
        else:
            shortestPath[x-1,y] = shortestPath[x,y] + [[x,y]]
            queue.append([x-1,y])

    if y > 0 and [x,y-1] not in corrupted:
        if (x,y-1) in shortestPath.keys():
            if len(shortestPath[x,y-1]) > len(shortestPath[x,y])+1:
                shortestPath[x,y-1] = shortestPath[x,y] + [[x,y]]
                queue.append([x,y-1])
        else:
            shortestPath[x,y-1] = shortestPath[x,y] + [[x,y]]
            queue.append([x,y-1])
    
    return queue, shortestPath


file = open("PuzzleInput.txt", "r").read().split("\n")
part = 2
corrupted = []

if part == 1:
    for i in range(0,1024):
        corrupted.append([int(file[i].split(",")[0]) , int(file[i].split(",")[1])])
    
    shortestPath = {}
    shortestPath[0,0] = []
    queue = [[0,0]]

    while len(queue) != 0:
        print(len(queue))
        next = queue.pop()
        queue, shortestPath = search(next[0],next[1],corrupted,shortestPath,queue)

    print(len(shortestPath[70,70]))

elif part == 2:
    pathFound = True
    min = 1025
    max = len(file)
    while min != max and min != max-1:
        a = int((min + max)/2)
        corrupted = []
        for i in range(0,a):
            corrupted.append([int(file[i].split(",")[0]) , int(file[i].split(",")[1])])

        pathFound = False
        shortestPath = {}
        shortestPath[0,0] = []
        queue = [[0,0]]

        while len(queue) != 0:
            #print(len(queue))
            next = queue.pop()
            queue, shortestPath = search(next[0],next[1],corrupted,shortestPath,queue)
            if (70,70) in shortestPath.keys():
                pathFound = True
                break
                
        if pathFound:
            min = a
            print("min")
        else:
            max = a
            print("max")

    print(file[max-1])
    