import sys
from collections import Counter

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

product = str(A * B * C)
num_counter = Counter(product)

for num in range(10):
    if str(num) not in num_counter.keys():
        print(0)
    else:
        print(num_counter[str(num)])
