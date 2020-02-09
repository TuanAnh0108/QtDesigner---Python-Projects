
import time
import math

def is_Prime_v2(n):
    if n == 1: 
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + int(max_divisor)):
        if n % d == 0:
            return False
    return True

for n in range(1, 21):
    print(n, is_Prime_v2(n))
