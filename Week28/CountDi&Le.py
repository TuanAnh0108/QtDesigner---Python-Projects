i = 0  # Declare the count variables
j = 0
String = input("Enter the text here: ")  # Input the text
for x in String:  # Loop through all the letters in the text
    if x.isdigit():  # Check if the letter is number
        j = j + 1
    if x.isalpha():  # Check if the letter is alphabet
        i = i + 1
# Print out the values
print("Letters {}".format(i))
print("Digits {}".format(j))
