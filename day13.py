file = open("PuzzleInput.txt", "r").read()
clawMachines = file.split("\n\n")
part = 2    
sum = 0

for machine in clawMachines:
    split = machine.split("\n")
    buttonA = split[0].split(": ")[1].replace("X+","").replace("Y+","").split(", ")
    buttonB = split[1].split(": ")[1].replace("X+","").replace("Y+","").split(", ")
    prize = split[2].split(": ")[1].replace("X=","").replace("Y=","").split(", ")
    buttonA[0] = int(buttonA[0])
    buttonA[1] = int(buttonA[1])
    buttonB[0] = int(buttonB[0])
    buttonB[1] = int(buttonB[1])
    prize[0] = int(prize[0])
    prize[1] = int(prize[1])
    if part == 2:
        prize[0] += 10000000000000
        prize[1] += 10000000000000

    B = (prize[1]-(buttonA[1]/buttonA[0])*prize[0])/(buttonB[1]-(buttonA[1]/buttonA[0])*buttonB[0])
    A = (prize[0]-buttonB[0]*B)/buttonA[0]

    if abs(round(A)-A)<0.001:
        A = round(A)
    if abs(round(B)-B)<0.001:
        B = round(B)

    if int(A)==A and int(B)==B:
        sum+=3*A+B


print(sum)