N=int(input("Enter the count of the numbers that needs to be summed:"))
x=[]  # Stores the user input as a list
count = 0
#Ask the user the input
for i in range(1,N+1): 
   y=int(input())
   x.append(y)
#Calculate how many zeros
for ind in range(0, N):
    if (x[ind] == 0):
        count = count + 1
print(count)


