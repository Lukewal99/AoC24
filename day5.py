def partOne(updates, rulesDict):
    correctUpdates = []
    for update in updates:
        correctOrder = True
        printedPages = []
        updatedPages = update.split(",")
        for updatedPage in updatedPages:
            if updatedPage in rulesDict.keys():
                #has a dependency
                followsDependencies = True
                dependencies = rulesDict[updatedPage]
                for dependency in dependencies:
                    if(dependency in updatedPages) :
                        if(dependency in printedPages)== False:
                            # page is in wrong order
                            followsDependencies = False
                            correctOrder = False
                            break
                if(followsDependencies):
                    printedPages.append(updatedPage)
                else:
                    break
            else:
                printedPages.append(updatedPage)
        if (correctOrder):
            correctUpdates.append(printedPages)
    return correctUpdates

def partTwo(updates, rulesDict):
    correctUpdates = []
    for update in updates:
        correctOrder = True
        printedPages = []
        updatedPages = update.split(",")
        for updatedPage in updatedPages:
            if (updatedPage in printedPages) == False:  
                if updatedPage in rulesDict.keys():
                    #has a dependency 
                    dependencies = rulesDict[updatedPage]
                    for dependency in dependencies:
                        if(dependency in updatedPages) :
                            if(dependency in printedPages)== False:
                                # page is in wrong order
                                correctOrder = False
                                printedPages = rearrangePages(updatedPages, dependency, rulesDict, printedPages)
                    printedPages.append(updatedPage)
                else:
                    printedPages.append(updatedPage)

        if (correctOrder == False):
            correctUpdates.append(printedPages)
    return correctUpdates

def rearrangePages(updatedPages, updatedPage, rulesDict, printedPages):
    if updatedPage in rulesDict.keys():
        #has a dependency 
        dependencies = rulesDict[updatedPage]
        for dependency in dependencies:
            if(dependency in updatedPages) :
                if(dependency in printedPages)== False:
                    # page is in wrong order
                    printedPages = rearrangePages(updatedPages, dependency, rulesDict, printedPages)
        printedPages.append(updatedPage)
    else:
        printedPages.append(updatedPage)

    return printedPages
    
file = open("PuzzleInput.txt", "r").read()
part = 2

rulesT, updatesT = file.split("\n\n")
rules = rulesT.split("\n")
updates = updatesT.split("\n")

rulesDict = {}
for rule in rules:
    dependency, page = rule.split("|")
    if page in rulesDict.keys():
        a = list(rulesDict[page])
        a.append(dependency)
        rulesDict[page] = a
    else:
        rulesDict[page] = [dependency]

correctUpdates = partOne(updates, rulesDict)

correctedUpdates = partTwo(updates, rulesDict)

sum = 0
if part == 1:
    for correctUpdate in correctUpdates:
        a = len(correctUpdate)
        b = int(a/2)
        c = int(correctUpdate[b])
        sum += c
elif part == 2:
    for correctedUpdate in correctedUpdates:
        a = len(correctedUpdate)
        b = int(a/2)
        c = int(correctedUpdate[b])
        sum += c

print(sum)