def search(x,y,map,trailheadsRatings,trailheadScore):
    if x-1 >= 0:
        if int(map[y][x-1]) == int(map[y][x])+1:
            if map[y][x-1] == '9':
                trailheadScore = trailheadScore+1
                if str(y) + " " + str(x-1) not in trailheadsRatings.keys():
                    trailheadsRatings[str(y) + " " + str(x-1)] = 1
                else:
                    trailheadsRatings[str(y) + " " + str(x-1)] += 1
                
            else:
                trailheadsRatings, trailheadScore = search(x-1,y,map,trailheadsRatings,trailheadScore)  
    if y-1 >= 0:
        if int(map[y-1][x]) == int(map[y][x])+1:
            if map[y-1][x] == '9':
                trailheadScore = trailheadScore+1
                if str(y-1) + " " + str(x) not in trailheadsRatings.keys():
                    trailheadsRatings[str(y-1) + " " + str(x)] = 1
                else:
                    trailheadsRatings[str(y-1) + " " + str(x)] += 1
                
            else:
                trailheadsRatings, trailheadScore = search(x,y-1,map,trailheadsRatings,trailheadScore) 

    if x+1 < len(map[y]):
        if int(map[y][x+1]) == int(map[y][x])+1:
            if map[y][x+1] == '9':
                trailheadScore = trailheadScore+1
                if str(y) + " " + str(x+1) not in trailheadsRatings.keys():
                    trailheadsRatings[str(y) + " " + str(x+1)] = 1
                else:
                    trailheadsRatings[str(y) + " " + str(x+1)] += 1
            else:
                trailheadsRatings, trailheadScore = search(x+1,y,map,trailheadsRatings,trailheadScore) 
    if y+1 < len(map):
        if int(map[y+1][x]) == int(map[y][x])+1:
            if map[y+1][x] == '9':
                trailheadScore = trailheadScore+1
                if str(y+1) + " " + str(x) not in trailheadsRatings.keys():
                    trailheadsRatings[str(y+1) + " " + str(x)] = 1
                else:
                    trailheadsRatings[str(y+1) + " " + str(x)] += 1
            else:
                trailheadsRatings, trailheadScore = search(x,y+1,map,trailheadsRatings,trailheadScore) 
    return trailheadsRatings, trailheadScore


file = open("PuzzleInput.txt", "r").read()
map = file.split("\n")
partOne = 0
partTwo = 0

for y in range(0,len(map)):
    for x in range(0,len(map[y])):
        if map[y][x] == '0':
            ratings, score = search(x,y,map,{},0)

            partOne += score
            for rating in ratings.values():
                partTwo+= rating

print(partOne)
print(partTwo)