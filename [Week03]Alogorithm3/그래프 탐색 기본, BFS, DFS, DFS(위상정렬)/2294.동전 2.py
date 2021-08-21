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


# 시간초과
import sys
from collections import deque

def bfs(n, cnt):
    global ans
    queue = deque([[n, cnt]])

    while queue:
        remain, cnt = queue.popleft()
        if remain == 0:
            ans = min(ans, cnt)
        for i in coins:
            if remain - i >= 0 and check[(remain - i)]:
                check[remain - 1] = False
                queue.append([remain - i, cnt + 1])
                
        
n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
check = [True for _ in range(n + 1)]
cnt = 0
ans = float('inf')
bfs(k, cnt)
print(ans)
