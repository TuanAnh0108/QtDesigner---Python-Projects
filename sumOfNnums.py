N=int(input("Enter the count of the numbers that needs to be summed:"))
x=[]  # Stores the user input as a list
for i in range(1,N+1): 
   y=int(input())
   x.append(y)
#Calculate the sum
Sum_of_Numbers= sum(x)
print(Sum_of_Numbers)