#Declare the variables
num = []
sum = 0
#Ask user for input
for i in range(6):
    num.append(input())

Time1 = num[0]*3600 + num[1]*60 + num[2]
Time2 = num[3]*3600 + num[4]*60 + num[5]
#Calculate the difference 
Difference = Time2 - Time1
#Print the result
print(Difference)

