NumCard = int(input("Enter the number of cards here: "))
x1 = [] #Store the input cards
sum1 = 0
#Ask user for input
for y in range(0,NumCard - 1):
    num = int(input())
    x1.append(num)
    sum1 = sum1 + x1[y]

x2 = [] #Store the total cards from 0 to NumCard
sum2 = 0
for i in range(0, NumCard+1):
    x2.append(i)
    sum2 = sum2 + x2[i]

#The lost card will be equal to the difference of 2 sums
LostCard = sum2 - sum1
print(LostCard)
    
