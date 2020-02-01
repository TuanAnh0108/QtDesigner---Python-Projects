#Declare the variables
position = []
#Ask user for input
for i in range(4):
    position.append(input())
#Check if the rock can move to the last position
if(position[0] == position[2] or position[1] == position[3]):
    print("YES")
else:
    print("NO")