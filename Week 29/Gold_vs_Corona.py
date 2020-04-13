# Import all the libraries
import matplotlib.pyplot as pyplot
import csv
from scipy.stats import spearmanr
from scipy.stats import pearsonr

# Append all the data in the csv file to a list
with open("total_cases.csv") as dt_corona:
    data_C = []
    data_C_total = []
    day_number = []
    values = csv.reader(dt_corona, delimiter=",")  # Divide the elements by ","
    for row in values:
        data_C.append(row)
    for y in range(len(data_C)):
        day_number.append(y)
    for i in range(len(data_C)):
        total_case_day = data_C[i][1]
        data_C_total.append(total_case_day)
    data_C_total = data_C_total[1:]
    total_cases = [int(j) for j in data_C_total]

with open("Gold_Price.csv") as dt_gold:
    data_G = []
    gold_price_total = []
    values = csv.reader(dt_gold, delimiter=",")  # Divide the elements by ","
    for row in values:
        data_G.append(row)
    for i in range(len(data_G)):
        gold_price_day = data_G[i][1]
        gold_price_total.append(gold_price_day)
    gold_price = [float(j) for j in gold_price_total]


print(total_cases)
print(gold_price)
# Calculate the correlation coefficient
corr, _ = pearsonr(total_cases, gold_price)
print(corr)  # The result is -0.028327711184862943 => variables change in opposite directions
# => The oil demand decreases because of the corona virus => The gold price decreases as the total cases increase

pyplot.plot(total_cases, gold_price)
pyplot.title("Cases vs Gold")
pyplot.ylabel('')
pyplot.show()
