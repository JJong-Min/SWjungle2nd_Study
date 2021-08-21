# 물이 먼저 들어가야한다.
# 시간을 count해줘야한다.
# 고슴도치의 방문위치를 check해야한다.
import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline()) for _ in range(r)]
check = [[True for _ in range(c)] for _ in range(r)]
queue = deque([])
cnt = 0
success = False

for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            queue.append(['*', cnt, i, j])

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            queue.append(['S', cnt, i, j])
            check[i][j] = False

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while queue:
    what, cnt, now_r, now_c = queue.popleft()
    for i in range(4):
        new_r, new_c = now_r + dx[i], now_c + dy[i]
        if 0 <= new_r < r and 0 <= new_c < c:
            if what == '*':
                if graph[new_r][new_c] == '.':
                    graph[new_r][new_c] = '*'
                    queue.append([what, cnt + 1, new_r, new_c])

            else:
                if graph[new_r][new_c] == '.' and check[new_r][new_c]:
                    queue.append([what, cnt + 1, new_r, new_c])
                    check[new_r][new_c] = False
                elif graph[new_r][new_c] == 'D':
                    success = True
                    break
    if success:
        break

if success:
    print(cnt + 1)
else:
    print("KAKTUS")
                    
                
                
