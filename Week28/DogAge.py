Age_dy = 0
Age_hy = int(input())  # Input the age of the dog in human year
for i in range(Age_hy):
    if i < 2:  # If the dog's age <= 2
        Age_dy = Age_dy + 10.5
    else:  # If the dos's age > 2
        Age_dy = Age_dy + 4
print("The dog's age in dog's year is {}".format(Age_dy))  # Print out the result
