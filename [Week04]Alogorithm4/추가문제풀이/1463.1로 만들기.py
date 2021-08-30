# bfs
'''
import sys
from collections import deque


def bfs(n, cnt):
    queue = deque([[n, cnt]])
    while queue:
        n, cnt = queue.popleft()
        if n % 3 == 0 and check[n // 3]:
            if n // 3 == 1:
                return cnt + 1
            else:
                check[n // 3] = False
                queue.append([n // 3, cnt + 1])
        
        if n % 2 == 0 and check[n // 2]:
            if n // 2 == 1:
                return cnt + 1
            else:
                check[n // 2] = False
                queue.append([n // 2, cnt + 1])

        if check[n - 1]:
            if n - 1 == 1:
                return cnt + 1
            else:
                check[n - 1] = False
                queue.append([n - 1, cnt + 1])
   
    
n = int(sys.stdin.readline())

check = [True for _ in range(n + 1)]
if n == 1:
    print(0)
else:
    print(bfs(n, 0))
'''
# dp(bottom up)
import sys

dp = [0, 0]
for i in range(2, int(sys.stdin.readline()) + 1):
    dp.append(dp[i - 1] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i %2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[-1])
