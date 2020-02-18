import matplotlib.pyplot as pyplot
import math

#1000RandomNums
x = [i for i in range(0, 1000)]
y = []
sum = 0
for m in range(0, 1000):
    h = random.randint(1, 100)
    y.append(h)
#Graph the xy
pyplot.plot(x, y)
pyplot.xlabel('x')
pyplot.ylabel('y')


#Calculate the average
for nums in y:
    sum = sum + nums
average = sum / len(y)
print(average)


#WaveFunction 

x = []
y = []
min = -10

for i in range(2000):
    x.append(min + 0.01*(i+1))
    y.append(14 * math.sin(0.5 * i))

pyplot.plot(x, y)
pyplot.xlabel('x')
pyplot.ylabel('$y = 14*sin(0.5x)')

#Sin Function
x = [i for i in range(-10, 10)]
y = [math.sin(i) ** 2 for i in x ]

pyplot.plot(x, y)
pyplot.xlabel('x')
pyplot.ylabel('$y = sin(x)^2x$ ')

#Bubble Sort
def bubbleSort(ar):
   n = len(ar)
   # Traverse through all array elements
   for i in range(n):
   # Last i elements are already in correct position
      for j in range(0, n-i-1):
      # Swap if the element found is greater than the next element
        if ar[j] > ar[j+1] :
             ar[j], ar[j+1] = ar[j+1], ar[j]
bubbleSort(y)
for i in range(len(y)):
   print (ar[i])

