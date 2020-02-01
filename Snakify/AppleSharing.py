#Declare the variables & ask user for input
numApples = int(input("Enter the number of apples here: \n"))
numStus = int(input("Enter the number of students here: \n"))

NumAppleEStu = numApples / numStus
RemainApple = numApples % numStus

print("The number of apples for each student is: {}".format(NumAppleEStu))
print("The number of remaining apples is: {}".format(RemainApple))
