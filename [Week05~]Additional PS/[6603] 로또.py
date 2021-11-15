import sys
from itertools import combinations
while True:
    n = list(map(int, sys.stdin.readline().split()))
    k = n[0]
    if k == 0:
        break
    n = n[1:]
    comb_n = list(combinations(n, 6))
    for comb in comb_n:
        print(*comb)

    print()
