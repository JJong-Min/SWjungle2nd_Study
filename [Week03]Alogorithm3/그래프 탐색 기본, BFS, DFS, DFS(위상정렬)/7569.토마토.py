import sys
from collections import deque


M, N, H = map(int, sys.stdin.readline().split())
graph = []
queue = deque([])

for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(M):
            if tmp[j][k] == 1:
                queue.append([i, j, k])
    graph.append(tmp)


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0 ,0]
dz = [0, 0, 0, 0, 1, -1]

while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and graph[nx][ny][nz] == 0:
            graph[nx][ny][nz] = graph[x][y][z] + 1
            queue.append([nx, ny, nz])

day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))
print(day - 1)


'''
import sys
from collections import deque

def bfs(i, j, n, m, h):
    queue = deque([[i, j]])
    dx = [-1, 1, 0, 0, n, -n]
    dy = [0, 0, 1, -1, 0 ,0]
    while queue:
        x, y = queue.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n * h and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

                
M, N, H = map(int, sys.stdin.readline().split())
graph = []
for i in range(N * H):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(N * H):
    for j in range(M):
        if graph[i][j] == 1:
            bfs(0, 0, N, M, H)

print(graph)
'''
