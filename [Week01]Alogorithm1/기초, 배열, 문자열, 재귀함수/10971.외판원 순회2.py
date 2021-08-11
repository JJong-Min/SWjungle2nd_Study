import sys
from itertools import permutations

def main():
    N = int(sys.stdin.readline())
    arr = []

    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))


    order_nums = permutations(range(N))
    final_cost = 1000000 * N

    for order_num in order_nums:
        if arr[order_num[-1]][order_num[0]] == 0:
            continue
        check = False
        cost = 0

        for idx in range(len(order_num) - 1):
            if arr[order_num[idx]][order_num[idx + 1]] == 0:
                check = True
                break

            cost += arr[order_num[idx]][order_num[idx + 1]]

            if cost >= final_cost:
                check = True
                break

        if check:
            continue

        cost += arr[order_num[-1]][order_num[0]]
        final_cost = min(final_cost, cost)

    print(final_cost)

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
        from_v = order_num[idx]
        to_v = order_num[idx+1]
        if arr[from_v][to_v] == 0:
            flag = True
            break
        cost += arr[from_v][to_v]
        '''
        if arr[order_num[idx]][order_num[(idx + 1)]] != 0:
            cost += arr[order_num[idx]][order_num[(idx + 1)]]
        
        else:
            check = True
            break
        '''
        if final_cost <= cost:
            check = True
            break
        
    if check:
        continue
        
    cost += arr[order_num[-1]][order_num[0]]
    final_cost = min(cost, final_cost)

print(final_cost)
