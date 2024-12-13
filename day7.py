file = open("PuzzleInput.txt", "r").read()
callibrations = file.split("\n")
part = 2
sum = 0
for callibration in callibrations:
    result = int(callibration.split(": ")[0])
    operands = callibration.split(": ")[1].split(" ")
    possibleResults = [int(operands[0])*int(operands[1]),int(operands[0])+int(operands[1])]
    if part == 2:
        possibleResults.append(int(str(operands[0])+str(operands[1])))
    for i in range(2,len(operands)):
        possibleResultsTemp = []
        operand = int(operands[i])
        for possibleResult in possibleResults:
            possibleResultsTemp.append(possibleResult*operand)
            possibleResultsTemp.append(possibleResult+operand)
            if part == 2:
                possibleResultsTemp.append(int(str(possibleResult)+str(operand)))
        possibleResults = possibleResultsTemp.copy()
    if result in possibleResults:
        sum+=result
print(sum)