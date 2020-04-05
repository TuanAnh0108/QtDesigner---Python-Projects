# Import all the libraries
import matplotlib.pyplot as pyplot
import csv

# Append all the data in the csv file to a list
with open("total_cases.csv") as dt:
    data = []
    values = csv.reader(dt, delimiter=",")   # Divide the elements by ","
    for row in values:
        data.append(row)

    # Show the total cases of all the countries
    day_number = []   # The number of days list
    total_case = []   # The total cases for each day list
    vietnam = []     # The case in each day in Vietnam list
    total_case_day = 0
    for i in range(len(data)):   # Loops through the data list
        day_number.append(i)
        for z in range(len(data[1])):           # Loops through the nested lists
            if data[i][z].isdigit():            # If the elements are numbers => They are the numbers of cases
                total_case_day = total_case_day + int(data[i][z])       # Calculate the total cases for each day

        total_case.append(total_case_day)
        total_case_day = 0

    # Show the total case of Vietnam
    for i in range(len(data)):
        for z in range(len(data[0])):
            if data[0][z] == "Vietnam":                 # Found the index of Vietnam
                Vietnam_index = z
                if i > 0:                               # The fist nested loop is Name of country so start from next one
                    vietnam.append(data[i][Vietnam_index])
                    for n in range(len(vietnam)):
                        if vietnam[n] == '':
                            vietnam[n] = '0'
                    vietnam = [int(j) for j in vietnam]  # Convert all the elements in the list to integer type

# Show the diagram
pyplot.plot(day_number)
pyplot.plot(total_case)
pyplot.plot(vietnam, color='red')
pyplot.title("Cases")
pyplot.xlabel('Day')
pyplot.ylabel('Number of case')
pyplot.show()

