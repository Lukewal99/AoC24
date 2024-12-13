def search(map, i, j):
    count = 0
    try: #NW
        if(i-3 >= 0 and j-3 >= 0):
            if map[i-1][j-1] == 'M' and map[i-2][j-2] == 'A' and map[i-3][j-3] == 'S':
                count +=1
    except:
        print('')
    try: #N
        if(i-3 >= 0):
            if map[i-1][j] == 'M' and map[i-2][j] == 'A' and map[i-3][j] == 'S':
                count +=1
    except:
        print('')
    try: #NE
        if(i-3 >= 0 and j+3 < len(map[i])):
            if map[i-1][j+1] == 'M' and map[i-2][j+2] == 'A' and map[i-3][j+3] == 'S':
                count +=1
    except:
        print('')

    try: #W
        if(j-3 >= 0):
            if map[i][j-1] == 'M' and map[i][j-2] == 'A' and map[i][j-3] == 'S':
                count +=1
    except:
        print('')
    try: #E
        if(j+3<len(map[i])):
            if map[i][j+1] == 'M' and map[i][j+2] == 'A' and map[i][j+3] == 'S':
                count +=1
    except:
        print('')

    try: #SW
        if(i+3 < len(map) and j-3 >= 0):
            if map[i+1][j-1] == 'M' and map[i+2][j-2] == 'A' and map[i+3][j-3] == 'S':
                count +=1
    except:
        print('')
    try: #S
        if(i+3 < len(map)):
            if map[i+1][j] == 'M' and map[i+2][j] == 'A' and map[i+3][j] == 'S':
                count +=1
    except:
        print('')
    try: #SE
        if(i+3 < len(map) and j+3 < len(map[i])):
            if map[i+1][j+1] == 'M' and map[i+2][j+2] == 'A' and map[i+3][j+3] == 'S':
                count +=1
    except:
        print('')
    return count


file = open("PuzzleInput.txt", "r").read()
part = 2
sum = 0

map = file.split("\n")

if part == 1:
    for i in range (0,len(map)):
        for j in range (0,len(map[0])):
            if(map[i][j] == 'X'):
                count = search(map,i,j)
                sum += count
                map[i] = map[i][0:j] + str(count) + map[i][j+1:len(map[i])]
        
elif part == 2:
    for i in range (1,len(map)-1):
        for j in range (1,len(map[0])-1):
            if(map[i][j] == 'A'):
                if(map[i-1][j-1] == 'M' and map[i+1][j+1] == 'S'):
                    if((map[i+1][j-1] == 'M' and map[i-1][j+1] == 'S') or (map[i-1][j+1] == 'M' and map[i+1][j-1] == 'S')):
                        sum+=1
                        
                elif(map[i+1][j+1] == 'M' and map[i-1][j-1] == 'S'):
                    if((map[i+1][j-1] == 'M' and map[i-1][j+1] == 'S') or (map[i-1][j+1] == 'M' and map[i+1][j-1] == 'S')):
                        sum+=1
                        

print(sum)