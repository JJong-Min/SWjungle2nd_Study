import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[sys.maxsize] * (m + 1)]

for _ in range(n):
    heights = [sys.maxsize] + list(map(int, sys.stdin.readline().split()))
    graph.append(heights)

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

dx = [-1, 0]
dy = [0, -1]

for i in range(1, n + 1):
    for j in range(1, m + 1):

        if i == j == 1:
            dp[i][j] = 1
        else:
            for k in range(2):
                nx, ny = i + dx[k], j + dy[k]
                if graph[i][j] < graph[nx][ny]:
                    dp[i][j] += dp[nx][ny]
            
            for k in range(2):
                nx, ny = i + dx[k], j + dy[k]
                if graph[nx][ny] < graph[i][j]:
                    dp[nx][ny] += dp[i][j]

print(dp[n][m])