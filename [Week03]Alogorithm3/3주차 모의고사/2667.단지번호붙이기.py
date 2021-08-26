import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, cnt):
    queue = deque([[x, y]])
    house_num = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                house_num += 1
                graph[nx][ny] = cnt
                queue.append([nx, ny])

    return house_num

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

cnt = 1
houses = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1
            graph[i][j] = cnt
            houses.append(bfs(i, j, cnt))


print(cnt - 1)
if houses:
    houses.sort()
    for house in houses:
        print(house)
