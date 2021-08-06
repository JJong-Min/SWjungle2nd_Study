import sys
import math

def is_prime_number(n):
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
N = int(sys.stdin.readline())
numbers = map(int, sys.stdin.readline().split())
count = 0

for i in numbers:
    if is_prime_number(i):
        count += 1

print(count)
    
