# 시간초과(dfs)
'''
import sys
from collections import defaultdict, deque

def change_askii(alphabet):
    return ord(alphabet) % 65

def dfs(i, j, cnt):
    global ans
    ans = max(ans, cnt)
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < r and 0 <= ny < c and not check[change_askii(graph[nx][ny])]:
            check[change_askii(graph[nx][ny])] = True
            cnt += 1
            dfs(nx, ny, cnt)
            check[change_askii(graph[nx][ny])] = False
            cnt -= 1

    
            
r, c = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(r)]

for i in range(r):
    input_val = sys.stdin.readline().rstrip()
    for j in input_val:
        graph[i].append(j)
check = [False for _ in range(26)]
check[change_askii(graph[0][0])] = True
ans = 0
dfs(0, 0, 1)
print(ans)
'''

# BFS
import sys
from collections import deque

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def bfs():
    result = 1
    queue = set([(0, 0, board[0][0])])

    while queue: 
        x, y, visited = queue.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in visited:
                next_visited = visited + board[nx][ny]
                queue.add((nx, ny, next_visited))
                result = max(result,len(next_visited))

    return result
  
r, c = map(int, sys.stdin.readline().split())
board=[list(sys.stdin.readline()) for _ in range(r)]

print(bfs())

# DFS (pypy)
import sys

def dfs(x, y, cnt):
    global ans
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and done[G[ny][nx]] == 0:
            if cnt + 1 > ans:
                ans = cnt + 1
                if ans == 26:
                    print(26)
                    exit(0)
            done[G[ny][nx]] = 1
            dfs(nx, ny, cnt + 1)
            done[G[ny][nx]] = 0
​
​
R, C = map(int, sys.stdin.readline().split())
G = [list(map(lambda x: ord(x) - 65, input())) for _ in range(R)]
done = [0] * 26
done[G[0][0]] = 1
dx = [0, 0, -1, 1]  # 상하좌우
dy = [-1, 1, 0, 0]
ans = 1
dfs(0, 0, 1)
print(ans)
