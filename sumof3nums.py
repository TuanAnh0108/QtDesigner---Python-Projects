#Declare the variables
num = []
sum = 0
#Ask user for input
for i in range(3):
    num.append(input("Enter numbers here: \n"))
#Calculate the sum
for ind in num:
    sum += ind
#Print the result
print("The sum of given numbers is: {}".format(sum))