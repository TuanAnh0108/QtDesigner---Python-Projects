#Ask user for input
num = int(input("Please enter the number here: "))
#Calculate the previous and next numbers
PreNum = num - 1
NextNum = num + 1
#Print the result
print("The next number for the number {} is {}".format(num,NextNum))
print("The previous number for the number {} is {}".format(num,PreNum))