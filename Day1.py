file = open("PuzzleInput.txt", "r")
part = 2


nums0 = []
nums1 = []
sum = 0

for line in file.read().split("\n"):
    pairs = line.split("   ")
    nums0.append(int(pairs[0]))
    nums1.append(int(pairs[1]))

if part==1:
    nums0.sort()
    nums1.sort()
    
    for i in range(0, len(nums0)):
        sum += abs(nums0[i] - nums1[i])

    
elif part ==2:
    counts = {}
    for num in nums1:
        if num in counts.keys():
            counts[num] += 1 
        else:
            counts[num] = 1
    
    for num in nums0:
        try:
            sum += num * counts[num]
        except:
            continue

print(sum)