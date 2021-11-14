import sys
from itertools import product

n = int(sys.stdin.readline())
answer = 0
for i in range(1, 1000000):
    sub = i
    i = str(i)
    num = sum([int(j) for j in i])
    sub += num
    if sub == n:
        answer = i
        break

print(answer)


