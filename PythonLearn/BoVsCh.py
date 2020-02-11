import math
#input
finish = 10
distanceBolt = 100
initialVelocy = 0
cheetahAcc = 10
boltSpeed = 10

#Calculate the time that Bold and Cheetah finish the road
timeB = finish / boltSpeed
totalD = finish + distanceBolt
velocyB = finish / timeB
timeC =  math.sqrt(totalD * 2 / cheetahAcc)

#Check who is the winner
if timeB < timeC:
    print("Bolt is the winner")
else:
    print("Cheetah is the winner")



