#Declare the variables
num = []
#Ask user for input
for i in range(3):
    num.append(input())

if (num[2] % num[0] == 0 and num[2] / num[0] < num[1]) or (num[2] % num[1] == 0 and num[2] / num[1] < num[0]):
    print('YES')
else:
    print('NO')