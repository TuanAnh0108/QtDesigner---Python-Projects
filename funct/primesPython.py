
import time
import math

def is_Prime_v2(n):
    if n == 1:           #Check if the number is different from 1
        return False
    max_divisor = math.floor(math.sqrt(n))       #calculate the square of the given number
    for d in range(2, 1 + int(max_divisor)):      #loops through all the numbers from 2 to the square of given number
        if n % d == 0:                             #Check if the number is prime number or not
            return False
    return True

for n in range(1, 21):       
    print(n, is_Prime_v2(n))

 """
 Explain:
    When we check if the number is prime numbers or not, we check all the possible product of 2 numbers that equal to the given numbers.
 For any products that we found, after the border: product of its square, the numbers are just repeat itself and just changes the position.
 Hence, we just need to check the product that are before the border. 
    If the number is equal to 1, it will be false due to it is unit number. We use loops to check if n is prime numbers. N will be divided by 
 all the number d smaller than its square, if n % d equal zeros, => n is not prime numbers. Else, n is prime number
 """
