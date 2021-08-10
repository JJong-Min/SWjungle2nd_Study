import itertools
import sys
input = sys.stdin.readline
def main():
    n = int(input())
    costs = [[0]*n for _ in range(n)]
    for y in range(n):
        s = list(map(int, input().split()))
        for i in range(n):
            costs[y][i] = s[i]

    perms = itertools.permutations(range(n))
    ret = sys.maxsize
    for perm in perms:
        if costs[perm[-1]][perm[0]] == 0:
            continue
        cost = 0
        flag = True
        for i in range(n-1):
            from_v = perm[i]
            to_v = perm[i+1]
            if costs[from_v][to_v] == 0:
                flag = False
                break
            cost += costs[from_v][to_v]
            if cost >= ret:
                flag = False
                break
        if flag == False:
            continue
        cost += costs[perm[-1]][perm[0]]
        ret = min(ret, cost)

    print(ret)

main()


# 시간 초과
import sys
from itertools import permutations

N = int(sys.stdin.readline())
arr = [[0]*N for _ in range(N)]

for y in range(N):
    s = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        arr[y][i] = s[i]



order_nums = permutations(range(N))
final_cost = sys.maxsize

for order_num in order_nums:
    if arr[order_num[-1]][order_num[0]] == 0:
        continue
    cost = 0
    check = False
        
    for idx in range(N - 1):
        if final_cost <= cost:
            check = True
            break
        
        if arr[order_num[idx]][order_num[(idx + 1)]] != 0:
            cost += arr[order_num[idx]][order_num[(idx + 1)]]
        
        else:
            check = True
            break
    if check:
        continue
        
    cost += arr[order_num[-1]][order_num[0]]
    final_cost = min(cost, final_cost)

print(final_cost)
