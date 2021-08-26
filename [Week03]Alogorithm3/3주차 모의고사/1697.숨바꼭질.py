import sys
from collections import deque

def bfs(val, goal):
    queue = deque([[val, 0]])
    while queue:
        val, cnt = queue.popleft()
        if val == goal:
            return cnt
        if 0 <= val - 1 <= 100000 and check[val - 1]:
            check[val - 1] = False
            queue.append([val - 1, cnt + 1])
        if 0 <= val + 1 <= 100000 and check[val + 1]:
            check[val + 1] = False
            queue.append([val + 1, cnt + 1])
        if val * 2 <= 100000 and check[val * 2]:
            check[val * 2] = False
            queue.append([val * 2, cnt + 1])

n, k = map(int, sys.stdin.readline().split())
check = [True for _ in range(100001)]
check[n] = False
print(bfs(n, k))
