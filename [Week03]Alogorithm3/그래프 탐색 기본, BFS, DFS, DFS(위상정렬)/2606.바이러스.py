# bfs

import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
check = [True for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

check[1] = False
queue = deque([1])
cnt = 0
while queue:
    computer = queue.popleft()
    cnt += 1
    for i in graph[computer]:
        if check[i]:
            check[i] = False
            queue.append(i)

print(cnt - 1)

# dfs
import sys

def dfs(i):
    cnt = 0
    for j in graph[i]:
        if check[j]:
            check[j] = False
            cnt += 1
            cnt += dfs(j)

    return cnt

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

check = [True for _ in range(n + 1)]
check[1] = False
print(dfs(1))
