'''
# 시간초과
import sys
from collections import deque

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(i, j):
    queue = deque([(i, j, 1)])
    ans = 1
    while queue:
        x, y, cnt = queue.popleft()
        ans = max(ans, cnt)
        visited[x][y] = 1
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and forest[x][y] < forest[nx][ny]:
                queue.append((nx, ny, cnt + 1))
    return ans       
        
n = int(sys.stdin.readline())
forest = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 1
for i in range(n):
    for j in range(n):
        visited = [[0 for _ in range(n)] for _ in range(n)]
        move = bfs(i, j)
        ans = max(move, ans)

print(ans)
'''

import sys

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n = int(sys.stdin.readline())
forest = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]
ans = 0

def dfs(x, y):
    if dp[x][y] == -1:
        dp[x][y] = 0

        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if 0 <= nx < n and 0 <= ny < n and forest[nx][ny] > forest[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny))

    return dp[x][y] + 1

for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)
