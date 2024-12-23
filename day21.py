def findSequence(seqIn):
    #x,y
    currentPos = [2,0]
    seqOut = ""

    if "|" in seqIn:
        metaButtons = seqIn.split("|")[0:-2]
        for metaButton in metaButtons:
            if metaButton in cache.keys():
                seqOut += cache[metaButton]
            else:
                temp = ""
                for button in metaButton:
                    neededPos = [0,0]
                    if button in ['<','v','>']:
                        neededPos[1] = 1

                    if button in ['^','v']:
                        neededPos[0] = 1
                    elif button in ['>','A']:
                        neededPos[0] = 2

                    if currentPos[1] > neededPos[1]:
                        # up
                        if currentPos[0] > neededPos[0]:
                            # <^ or <<^ or <^^ or <<^^
                            temp += "<"*(currentPos[0] - neededPos[0])
                            temp += "^"*(currentPos[1] - neededPos[1])

                        elif currentPos[0] < neededPos[0]:
                            # >^
                            temp += ">"*abs(currentPos[0] - neededPos[0])
                            temp += "^"*(currentPos[1] - neededPos[1])

                        else:
                            # ^
                            temp += "^"*(currentPos[1] - neededPos[1])

                    elif currentPos[1] < neededPos[1]:
                        # down
                        if currentPos[0] > neededPos[0]:
                            if currentPos[1] == 1 and neededPos[0] == [0]:
                                temp += "v"*abs(currentPos[1] - neededPos[1])
                                temp += "<"*(currentPos[0] - neededPos[0])
                            else:
                                # <v
                                temp += "<"*(currentPos[0] - neededPos[0])
                                temp += "v"*abs(currentPos[1] - neededPos[1])
            
                        elif currentPos[0] < neededPos[0]:
                            # v>
                            temp += "v"*abs(currentPos[1] - neededPos[1])
                            temp += ">"*abs(currentPos[0] - neededPos[0])

                        else:
                            # v
                            temp += "v"*abs(currentPos[1] - neededPos[1])
                            
                    else:
                        # L/R
                        if currentPos[0] > neededPos[0]:
                            # <
                            temp += "<"*(currentPos[0] - neededPos[0])
                        else:
                            # >
                            temp += ">"*abs(currentPos[0] - neededPos[0]) 

                    temp+= "A"
                    currentPos = neededPos
                cache[metaButton] = temp
                seqOut+=temp+"|"


    else:
        print("hm")
    return(seqOut)

codes = open("PuzzleInput.txt", "r").read().split("\n")
sum = 0
part = 2
global cache
cache = {}

for code in codes:
    #x,y
    currentPos = [2,3]
    keypadBot = ""
    for button in code:
        neededPos = [0,0]
        if button in ['4','5','6']:
            neededPos[1] = 1
        elif button in ['1','2','3']:
            neededPos[1] = 2
        elif button in ['0','A']:
            neededPos[1] = 3

        if button in ['8','5','2','0']:
            neededPos[0] = 1
        elif button in ['9','6','3','A']:
            neededPos[0] = 2

        if currentPos[1] > neededPos[1]:
            # up
            if currentPos[0] > neededPos[0]:
                if not(currentPos[1] == 3 and neededPos[0] == 0):
                    # <^ or <<^ or <^^ or <<^^
                    keypadBot += "<"*(currentPos[0] - neededPos[0])
                    keypadBot += "^"*(currentPos[1] - neededPos[1])
                else:
                    # ^<
                    keypadBot += "^"*(currentPos[1] - neededPos[1])
                    keypadBot += "<"*(currentPos[0] - neededPos[0])

            elif currentPos[0] < neededPos[0]:
                    # >^
                    keypadBot += ">"*abs(currentPos[0] - neededPos[0])
                    keypadBot += "^"*(currentPos[1] - neededPos[1])

            else:
                # ^
                keypadBot += "^"*(currentPos[1] - neededPos[1])

        elif currentPos[1] < neededPos[1]:
            # down
            if currentPos[0] > neededPos[0]:
                # <v
                keypadBot += "<"*(currentPos[0] - neededPos[0]) 
                keypadBot += "v"*abs(currentPos[1] - neededPos[1])  

            elif currentPos[0] < neededPos[0]:
                if currentPos[0] == 0 and neededPos[1] == 3:
                    keypadBot += ">"*abs(currentPos[0] - neededPos[0])
                    keypadBot += "v"*abs(currentPos[1] - neededPos[1])
                else:
                    # v>
                    keypadBot += "v"*abs(currentPos[1] - neededPos[1])
                    keypadBot += ">"*abs(currentPos[0] - neededPos[0])

            else:
                # v
                keypadBot += "v"*abs(currentPos[1] - neededPos[1])
                
        else:
            # L/R
            if currentPos[0] > neededPos[0]:
                # <
                keypadBot += "<"*(currentPos[0] - neededPos[0])
            else:
                # >
                keypadBot += ">"*abs(currentPos[0] - neededPos[0]) 

        keypadBot+= "A|"
        currentPos = neededPos

    arrowsBot = findSequence(keypadBot)
    if part == 2:
        for i in range(0,24):
            print(i)
            arrowsBot = findSequence(arrowsBot)
    me = findSequence(arrowsBot)
    print(str(len(me)) + "*" + str(code[0:3]) + "=" + str(len(me)*int(code[0:3])))
    sum += len(me)*int(code[0:3])
print(sum)  
