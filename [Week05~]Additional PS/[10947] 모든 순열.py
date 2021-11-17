import sys
from itertools import permutations

n = int(sys.stdin.readline())
n_list = [i for i in range(1, n + 1)]

permu_list = list(permutations(n_list, n))
for permu in permu_list:
    print(*permu)

