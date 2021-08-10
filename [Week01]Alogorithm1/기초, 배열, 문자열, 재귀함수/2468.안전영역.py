import sys

def check_nonsafe(point, N):
    check = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] <= point:
                check[i][j] = True

    return check

def dfs(x, y): 
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0<= nx < N and 0<= ny < N and (not check[nx][ny]) and (not visited[nx][ny]):
            dfs(nx, ny)

sys.setrecursionlimit(15000)            
N = int(sys.stdin.readline())
graph = []

for i in range(N):
    region_heights = list(map(int, sys.stdin.readline().split()))
    graph.append(region_heights)


ans = 1
for rain_point in range(1, 100):
    check = check_nonsafe(rain_point, N)
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    
    for i in range(N):
        for j in range(N):
            if (not check[i][j]) and  (not visited[i][j]):
                cnt += 1
                dfs(i, j)
                
    
    ans = max(ans, cnt)
print(ans)
