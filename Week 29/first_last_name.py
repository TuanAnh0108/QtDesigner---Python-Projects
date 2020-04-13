string = input("Enter first, last name and a number in here: ").split(sep=",")  # Input the value
with open("output.txt", "a") as out_file:   # Open the output file
    for i in range(3):
        out_file.write(("{}.{}{}@uwcisak.jp".format(str(string[0]), str(string[1]), int(i+1)) + "\n"))   # Print the
                                                                                            # data to the out put file
