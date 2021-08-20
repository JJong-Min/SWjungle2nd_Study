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