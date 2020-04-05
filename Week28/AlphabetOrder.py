list = []
text = input("Enter the text here: ")  # Input
for i in text.split(","):  # split the text when facing ","
    list.append(i)  # append it to the list
list.sort()  # sort the list
print(','.join(list))  # join the elements with "," again
