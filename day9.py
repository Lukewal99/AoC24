file = open("PuzzleInput.txt", "r").read()
data = True
part = 2
ID = 0
storage = []
sum = 0


for number in file:
    if number != '0':
        if data:
            if part == 1:
                for i in range(0,int(number)):
                    storage.append(str(ID))
            elif part ==2:
                storage.append((str(ID)+":")*int(number))
            ID+=1
        else:
            for i in range(0,int(number)):
                storage.append('.')
    data = not data
#print(storage)

if part == 1:
    j = len(storage)-1
    for i in range(0,len(storage)):
        while storage[j] == '.':
            j-=1
        if storage[i] == '.':
            storage[i] = storage[j]
            storage[j] = '.'
        if j <= i:
            storage[j] = storage[j+1]
            storage[j+1] = '.'
            break

    #print(storage)

    for i in range(1,j+1):
        sum+= i*int(storage[i])


if part == 2:
    i=0
    while i in range(0,len(storage)-1):
        if '.' in storage[i] and '.' in storage[i+1]:
            storage[i] += storage[i+1]
            storage.pop(i+1)
            i-=1
        i+=1

    
    i = len(storage)-1
    #print(storage)
    while i > 0:
        moved = False
        if ':' in storage[i]:
            lenRequired = len(storage[i].split(":"))-1
            for j in range(0,i):
                lenAvailable = len(storage[j])
                if '.' in storage[j] and lenAvailable >= lenRequired:
                    storage[j] = storage[i]
                    storage[i] = '.' * lenRequired
                    if lenAvailable!=lenRequired:
                        storage.insert(j+1,"."*(lenAvailable-lenRequired)) 
                    else:
                        i-=1
                    moved = True
                    break

        if moved:
            j=0
            while j in range(0,len(storage)-1):
                if '.' in storage[j] and '.' in storage[j+1]:
                    storage[j] += storage[j+1]
                    storage.pop(j+1)
                else:
                    j+=1
        else:
            i-=1

    storage = str(storage).replace("['","").replace("']","").replace("', '","").replace(".",":").split(":")
    for k in range(0,len(storage)):
        item = storage[k]
        if item != '':
            sum+= k*int(item)

    

print(sum)