import sys
from collections import deque
'''
def dfs(x):
    graph[x].sort()
    for i in graph[x]:
        if check[i]:
            check[i] = False
            print(i, end= " ")
            dfs(i)

    return
        

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

check = [True for _ in range(N + 1)]

check[V] = False
print(V, end=" ")
dfs(V)

print()

check = [True for _ in range(N + 1)]
queue = deque([V])
while queue:
    now_node = queue.popleft()
    check[now_node] = False
    print(now_node, end=" ")
    graph[now_node].sort()
    for i in graph[now_node]:
        if check[i]:
            queue.append(i)
'''

def dfs(x):
    graph[x].sort()
    for i in graph[x]:
        if check[i]:
            check[i] = False
            dfs_result.append(i)
            dfs(i)
    return
        

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

check = [True for _ in range(N + 1)]

check[V] = False
dfs_result = [V]
dfs(V)
print(*dfs_result)

check = [True for _ in range(N + 1)]
queue = deque([V])
check[V] = False
bfs_result = []
while queue:
    now_node = queue.popleft()
    bfs_result.append(now_node)
    graph[now_node].sort()
    for i in graph[now_node]:
        if check[i]:
            check[i] = False
            queue.append(i)

print(*bfs_result)
