import sys
from itertools import permutations

n, k = map(int, sys.stdin.readline().split())
kits = sys.stdin.readline().split()
comb_kits = list(permutations(kits))
answer = 0

for kit in comb_kits:
    weights = 500
    for _weight in kit:
        weights -= k
        if weights + int(_weight) < 500:
            break
        weights += int(_weight)
    else:
        answer += 1
print(answer)
