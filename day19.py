# WORKS FOR PART 1
#def contains(pattern):
#    if len(pattern) == 0:
#        return True
#    if pattern in invalidTowels:
#        return False
#    for i in range(min(maxTowelSize, len(pattern)), -1, -1):
#        test = pattern[0:i]
#        rest = pattern[i:len(pattern)]
#
#        elif test in towels and contains(rest):
#            if pattern not in towels:
#                towels.append(pattern)
#            return True
#
#    if pattern not in invalidTowels:
#        invalidTowels.append(pattern)
#    return False

def contains(pattern):
    possibleWays = 0

    if len(pattern) == 0 or (len(pattern) == 1 and pattern in towels):
        return 1
    if pattern in invalidTowels:
        return 0
    if pattern in comboTowels.keys():
        return comboTowels[pattern]


    for i in range(min(maxTowelSize, len(pattern)-1), 0, -1):
        test = pattern[0:i]
        rest = pattern[i:len(pattern)]

        if test not in invalidTowels and rest not in invalidTowels:

            if test in comboTowels.keys():
                if rest in comboTowels.keys():
                    possibleWays += comboTowels[test]*comboTowels[rest]
                else:
                    temp = contains(rest)
                    if rest in towels and len(rest) > 1:
                        temp+=1

                    if temp != 0:
                        comboTowels[rest] = temp
                        possibleWays += comboTowels[test] * temp
                    else:
                        invalidTowels.append(rest)

                return possibleWays

            elif test in towels:
                if rest in comboTowels.keys():
                    possibleWays += comboTowels[rest]
                else:
                    temp = contains(rest)
                    if rest in towels and len(rest) > 1:
                        temp+=1
                
                    if temp != 0:
                        comboTowels[rest] = temp
                        possibleWays += temp
                    else:
                        invalidTowels.append(rest)

    if possibleWays == 0 and pattern not in invalidTowels:
            invalidTowels.append(pattern)
    return possibleWays


file = open("PuzzleInput.txt", "r").read().split("\n\n")
global towels
towels = file[0].split(", ")

global comboTowels
comboTowels = {}
global invalidTowels
invalidTowels = []

patterns = file[1].split("\n")
sum = 0
part = 2

global maxTowelSize
maxTowelSize = 0
for towel in towels:
    if len(towel) > maxTowelSize:
        maxTowelSize = len(towel)

    

if part == 1:
    for pattern in patterns:
        if contains(pattern):
            sum+=1

elif part == 2:
    for pattern in patterns:
        sum+=contains(pattern)

print(sum)
#658,748,656,890 too low