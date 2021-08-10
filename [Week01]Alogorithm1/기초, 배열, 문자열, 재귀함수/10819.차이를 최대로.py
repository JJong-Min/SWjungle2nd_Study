import sys
from itertools import permutations

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

candidates = list(permutations(arr))
max_sum = 0

for candidate in candidates:
    candidate_sum = 0
    before_num = candidate[0]
    for idx in range(1, len(candidate)):
        candidate_sum += abs(before_num - candidate[idx])
        before_num = candidate[idx]

    max_sum = max(max_sum, candidate_sum)

print(max_sum)
