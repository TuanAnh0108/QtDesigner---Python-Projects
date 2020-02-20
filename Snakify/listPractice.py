1. Even Indices

# Declare the list
nums = []

# Input
confirmed = False
while not confirmed:
    num_in = input("Enter the numbers here: (or leave a blank to stop)")
    nums.append(num_in)
    if num_in == '':
        confirmed = True

for i in range(0, len(nums), 2):
    print(nums[i])

2. Even Elements

# Declare the list
nums = []

# Input
confirmed = False
while not confirmed:
    num_in = (input("Enter the numbers here: (or leave a blank to stop)"))
    if num_in == '':
        break
    nums.append(num_in)

#Print the result
for i in nums:
    if int(i) % 2 == 0:
        print(i)

3. Greater than previous

# Declare the list
nums = []

# Input
confirmed = False
while not confirmed:
    num_in = (input("Enter the numbers here: (or leave a blank to stop)"))
    if num_in == '':
        break
    nums.append(num_in)

for i in range(0, len(nums) - 1, 1):
    if nums[i + 1] > nums[i]:
        print(nums[i+1])
4. Neighbor of the same sign

# Declare the list
nums = []

# Input
confirmed = False
while not confirmed:
    num_in = (input("Enter the numbers here: (or leave a blank to stop)"))
    if num_in == '':
        break
    nums.append(num_in)

for i in range(0, len(nums) - 1, 1):
    if (int(nums[i + 1]) < 0 and int(nums[i]) < 0) or (int(nums[i + 1]) > 0 and int(nums[i]) > 0):
        print(nums[i], nums[i+1])
        break
5. Greater than neighbours

# Declare the list
nums = []
count = 0
# Input
confirmed = False
while not confirmed:
    num_in = (input("Enter the numbers here: (or leave a blank to stop)"))
    if num_in == '':
        break
    nums.append(num_in)

for i in range(1, len(nums) - 1, 1):
    if int(nums[i]) > int(nums[i + 1]) and (int(nums[i]) > int(nums[i - 1])):
        count += 1
print(count)


