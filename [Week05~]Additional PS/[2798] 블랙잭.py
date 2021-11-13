import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
subs = permutations(num_list, 3)
answer = 0

for sub in subs:
    sum_num = sum(sub)
    if sum_num <= m:
        answer = max(sum_num, answer)

print(answer)
