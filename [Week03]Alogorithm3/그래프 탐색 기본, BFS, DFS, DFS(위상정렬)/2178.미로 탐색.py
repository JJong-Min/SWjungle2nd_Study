import sys
from collections import deque

def bfs(i, j):
    queue = deque([[i, j]])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                queue.append([nx, ny])    
    
                
        
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
for i in range(N):
    input_val = sys.stdin.readline().rstrip()
    for j in input_val:
        graph[i].append(int(j))
bfs(0, 0)
print(graph[N-1][M-1])
