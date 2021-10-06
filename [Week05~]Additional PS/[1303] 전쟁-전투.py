import sys
from collections import deque

deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(i, j, color):
    queue = deque([[i, j, color]])
    cnt = 1
    while queue:
        x, y, color = queue.popleft()
        for i in range(4):
            nx = x + deltas[i][0]
            ny = y + deltas[i][1]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == color and check[nx][ny]:
                cnt += 1
                check[nx][ny] = False
                queue.append([nx, ny, color])
    return cnt ** 2

n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
check = [[True] * n for _ in range(m)]

b_power = 0
w_power = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == "B" and check[i][j]:
            check[i][j] = False
            b_power += bfs(i, j, "B")

        if graph[i][j] == "W" and check[i][j]:
            check[i][j] = False
            w_power += bfs(i, j, "W")
            
print(w_power, b_power)
