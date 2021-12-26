import sys
from collections import deque

def bfs(i, j, color):
    queue = deque([(i, j)])
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if 0 <= nx < n and 0 <= ny < n and image[nx][ny] == color and not visited[nx][ny]:
                queue.append((nx, ny))


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n = int(sys.stdin.readline())
image = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

ans1 = 0
ans2 = 0

visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            ans1 += 1
            bfs(i, j, image[i][j])

for i in range(n):
    for j in range(n):
        if image[i][j] == "R":
            image[i][j] = "G"
                
visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            ans2 += 1
            bfs(i, j, image[i][j])

print(ans1, ans2)
