import matplotlib.pyplot as plt

file = open("PuzzleInput.txt", "r").read()
robots = file.split("\n")
part = 2   

t = 100
width = 101
height = 103

quadOne = 0
quadTwo = 0
quadThree = 0
quadFour = 0

if part == 1:
    for robot in robots:
        posT, velT = robot.split(" ")
        pos = posT.replace("p=","").split(",")
        vel = velT.replace("v=","").split(",")
        pos = int(pos[0]),int(pos[1])
        vel = int(vel[0]),int(vel[1])

        pos = [(pos[0]+vel[0]*t)%width, (pos[1]+vel[1]*t)%height]
        
        
        if pos[0] < int(width/2):
            if pos[1] < int(height/2):
                quadOne+=1
            elif pos[1] > int(height/2):
                quadThree+=1
        elif pos[0] > int(width/2):
            if pos[1] < int(height/2):
                quadTwo+=1
            elif pos[1] > int(height/2):
                quadFour+=1
    print(quadOne*quadTwo*quadThree*quadFour)


if part == 2:
    t = 0
    while True:
        posS = []
        X = []
        Y = []
        
        for robot in robots:
            posT, velT = robot.split(" ")
            pos = posT.replace("p=","").split(",")
            vel = velT.replace("v=","").split(",")
            pos = int(pos[0]),int(pos[1])
            vel = int(vel[0]),int(vel[1])
            pos = [(pos[0]+vel[0]*t)%width, (pos[1]+vel[1]*t)%height]
            posS.append(pos)
            X.append(pos[0])
            Y.append(pos[1])
        
        for i in range(0,len(posS)):
            aX = posS[i][0]
            aY = posS[i][1]

            if [aX+1,aY] in posS and [aX+2,aY] in posS and [aX+3,aY] in posS and [aX+4,aY] in posS and [aX+5,aY] in posS and [aX+6,aY] in posS:
                print(t)
                plt.scatter(X,Y)
                plt.show()
        t+=1

        