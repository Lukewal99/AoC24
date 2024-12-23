def runProgram(registers):
    pointer = 0
    end = False
    output = ""

    while not end:
        comboLookup = [0,1,2,3,registers[0],registers[1],registers[2]]

        if pointer+1 >= len(program):
            end = True
        else:
            opcode = program[pointer]
            operand = int(program[pointer+1])
            if operand < 7:
                combo = comboLookup[operand]

            if opcode == '0': #adv
                registers[0] = int(registers[0]/pow(2,combo))
            elif opcode == '1': #bxl
                registers[1] = registers[1] ^ operand
            elif opcode == '2': #bst
                registers[1] = combo % 8
            elif opcode == '3': #jnz
                if registers[0] != 0:
                    pointer = operand-2
            elif opcode == '4': #bxc
                registers[1] = registers[1] ^ registers[2]
            elif opcode == '5': #out
                output+=str(combo%8) + ","
            elif opcode == '6': #bdv
                registers[1] = int(registers[0]/pow(2,combo))
            elif opcode == '7': #cdv
                registers[2] = int(registers[0]/pow(2,combo))
            else:
                print("wtf")
                end = True
            pointer+=2
    return(output)

def partTwo(a):
    registers = [a,0,0]
    pointer = 0
    end = False
    output = ''

    while not end:
        comboLookup = [0,1,2,3,registers[0],registers[1],registers[2]]

        if pointer+1 >= len(program):
            end = True
        else:
            opcode = program[pointer]
            operand = int(program[pointer+1])
            if operand < 7:
                combo = comboLookup[operand]

            if opcode == '0': #adv
                registers[0] = int(registers[0]/pow(2,combo))
            elif opcode == '1': #bxl
                registers[1] = registers[1] ^ operand
            elif opcode == '2': #bst
                registers[1] = combo % 8
            elif opcode == '3': #jnz
                if registers[0] != 0:
                    pointer = operand-2
            elif opcode == '4': #bxc
                registers[1] = registers[1] ^ registers[2]
            elif opcode == '5': #out
                output+=str(combo%8) + ","
            elif opcode == '6': #bdv
                registers[1] = int(registers[0]/pow(2,combo))
            elif opcode == '7': #cdv
                registers[2] = int(registers[0]/pow(2,combo))
            else:
                print("wtf")
                end = True
            pointer+=2
    return(output)

file = open("PuzzleInput.txt", "r").read().split("\n\n")
registers = file[0].replace("Register A: ","").replace("Register B: ","").replace("Register C: ","").split("\n")
for i in range(0,len(registers)):
    registers[i] = int(registers[i])
program = file[1].replace("Program: ","").split(",")
part = 2


i = 0

if part == 1:
    output = runProgram(registers)

elif part == 2:
    # Hand solved equivelant code
    #While A != 0
    # B = not(A%8) -- Last 3 of A
    # C = A RShift B
    # A = A RShift 3 -- Shift Tape along
    # Output not(B XOR C)


        
    for a in range(0b001000000000000000000,0b1000000000000000000000):
        #print(int(10000*a/2097152)/100)
        out = partTwo(a).split(",")
        out = out[0:len(out)-1]
        if program == out:
            print(a)
            break

    #UGHHH WHY ISNT THIS WORKING