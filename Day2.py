def part1(levels):
    prevDiff = int(levels[1])-int(levels[0])
    if (prevDiff == 0):
        direction = 0
    else:
        direction = prevDiff/abs(prevDiff)

    safe = True
    for i in range(0,len(levels)-1):
        diff = int(levels[i+1])-int(levels[i])
        if (abs(diff) > 3):
            safe = False
            break
        if(diff == 0):
            safe = False
            break
        elif((diff/abs(diff))!= direction):
            safe = False
            break

    if(safe):
        return 1
    else:
        return 0

file = open("PuzzleInput.txt", "r")
part = 2

reports = file.read().split("\n")

safeCount = 0
for report in reports:
    levels = report.split(" ")

    if part == 1:
        safeCount += part1(levels)



    elif part == 2:
        if part1(levels) == 1:
            safeCount += part1(levels)
        else:
            testCount = 0
            for j in range(0, len(levels)):
                testLevels = levels[0:j] + levels[j+1:len(levels)]
                testCount += part1(testLevels)

            if testCount >= 1:
                safeCount+=1
        
       
print(safeCount)