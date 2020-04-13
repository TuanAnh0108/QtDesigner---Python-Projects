import random
import string

n = int(input())  # Input the number of times generate the password


def random_password(number):
    letters = string.ascii_letters + '0123456789-^~=|¥#$%&()!{}[]@`+;:*<>,./?_'  # Assign all the letters, numbers and
                                                                                # symbols
    for i in range(number):
        print(''.join(random.choice(letters) for i in range(20)))  # Get random letter from letters do it 20
                                                                                # times (the length of password)


random_password(n)  # Print the result
