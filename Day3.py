import re

file = open("PuzzleInput.txt", "r").read()
part = 2
sum = 0

mulRE = "mul\([0-9]+,[0-9]+\)"
doRE = "do\(\)"
dontRE = "don't\(\)"
enabled = True

commands = ""
if part == 1:
    commands = re.findall(mulRE, file)
    for command in commands:
        pair = command.split("mul(")[1].split(")")[0].split(",")

        sum += int(pair[0]) * int(pair[1])

elif part == 2:
    find = mulRE+"|"+doRE+"|"+dontRE
    commands = re.findall(find, file)
    for command in commands:
        if command == "do()":
            enabled = True
        elif command == "don't()":
            enabled = False
        elif "mul" in command and enabled:
            pair = command.split("mul(")[1].split(")")[0].split(",")
            sum += int(pair[0]) * int(pair[1])


print(sum)