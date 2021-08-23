import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
degrees = [0 for _ in range(n + 1)]
check = [True for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    degrees[y] += 1

stack = []
for idx in range(1, n + 1):
    if degrees[idx] == 0:
        stack.append(idx)
        check[idx] = False

while stack:
    now_num = stack.pop()
    for i in graph[now_num]:
        if degrees[i] > 0:
            degrees[i] -= 1
        if degrees[i] == 0 and check[i]:
            stack.append(i)

    print(now_num, end=' ')


    
