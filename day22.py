file = open("PuzzleInput.txt", "r").read().split("\n")
sum = 0
part = 2

if part == 1:
    for secret in file:
        a = int(secret)
        for i in range(0,2000):
            a ^= (a*64)
            a %= 16777216
            a ^= (a // 32)
            a %= 16777216
            a ^= (a * 2048)
            a %= 16777216
        sum +=a
    print(sum)

elif part == 2:  
    
    diffArrays = {}
    for secret in file:
        print(file.index(secret))
        bananas = []
        diffs = []
        a = int(secret)
        prevBanana = a%10
        for x in range(0,2000):
            a ^= (a*64)
            a %= 16777216
            a ^= (a // 32)
            a %= 16777216
            a ^= (a * 2048)
            a %= 16777216
            dif = a%10 - prevBanana
            prevBanana = a%10
            bananas.append(a%10)
            diffs.append(dif)
        diffArrays[secret] = [bananas,diffs]


    maxSum = 0
    for i in range(9,-10,-1):
        for j in range(9,-10,-1):
            for k in range(9,-10,-1):
                for l in range(9,-10,-1):
                    if (i+j+k+l > 9) or (i+j+k+l < -9):
                        continue
                    sequence = [i,j,k,l]
                    print(sequence)
                    sum = 0


                    for key in diffArrays.keys():
                        diff = diffArrays[key]
                        if str(sequence).replace("[","").replace("]","") in str(diff[1]):
                            for m in range(3,2000):
                                if [diff[1][m-3],diff[1][m-2],diff[1][m-1],diff[1][m]] == sequence:
                                    sum+=diff[0][m]
                                    break

                    
                    maxSum = max(sum, maxSum)
    print(maxSum)

