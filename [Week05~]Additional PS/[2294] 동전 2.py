import sys
from collections import deque


n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
queue = deque([(k, 0)])
flag = False
while queue:
    remain_coin, cnt = queue.popleft()
    if remain_coin == 0:
        flag = True
        print(cnt)
        break

    for coin in coins:
        if remain_coin - coin >= 0:
            queue.append((remain_coin - coin, cnt + 1))

if not flag:
    print(-1)


import sys
from collections import deque
       
n, k = map(int, sys.stdin.readline().split())
check = [True for _ in range(k + 1)]
coins = set([int(sys.stdin.readline()) for _ in range(n)])
queue = deque()
for coin in coins:
    if coin <= k:
        queue.append((coin, 1))
        check[coin] = False

flag = True
while queue:
    val, cnt = queue.popleft()
    if val == k:
        print(cnt)
        flag = False
        break

    for coin in coins:
        if val + coin <= k and check[(val + coin)]:
            check[val+coin] = False
            queue.append((val + coin, cnt + 1))

if flag:
    print(-1)


import sys

n, k = map(int, sys.stdin.readline().split())
coins = sorted([int(sys.stdin.readline()) for _ in range(n)])
dp = [10001 for _ in range(k + 1)]
dp[0] = 0

for i in range(n):
    for j in range(coins[i], k + 1):
        dp[j] = min(dp[j], dp[j - coins[i]] + 1)
