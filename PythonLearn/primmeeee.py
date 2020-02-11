
import time
import math


def is_Prime(n):
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    if n == 1: 
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + int(max_divisor),2):
        if n % d == 0:
            return False
    return True

