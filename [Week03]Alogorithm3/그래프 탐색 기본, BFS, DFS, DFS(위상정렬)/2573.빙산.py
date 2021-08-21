'''
import sys
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
   queue = deque([[i, j]])
   melting_queue = deque([])
   while queue:
      x, y = queue.popleft()
      melt_cnt = 0
      for i in range(4):
         nx = x + dx[i]
         ny = y + dy[i]
         if 0 <= nx < x and 0 <= ny < y and check[nx][y]:
            if graph[nx][ny] != 0:
               check[nx][ny] = False
               queue.append([nx, ny])
            else:
               melt_cnt += 1
      if melt_cnt:
         melting_queue.append([x, y, melt_cnt])
   return melting_queue


########입력 받기#########   
n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
########################

######탐색#########
ans = 0
while True:
   check = [[True for _ in range(m)] for _ in range(n)]
   cnt = 0
   for i in range(n):
      for j in range(m):
         if graph[i][j] != 0 and check[i][j]:
            cnt += 1
            check[i][j] = False
            melt = bfs(i, j)
   #####빙산이 다 녹은 경우 확인##########       
            while melt:
               m_x, m_y, m = melt.popleft()
               graph[[m_x][m_y]] = max(graph[[m_x][m_y]] - m, 0)
   if cnt == 0:
      ans = 0
   elif cnt >= 2:
      break

   ans += 1
               
print(ans)
'''

import sys
from collections import deque, defaultdict

def bfs(i, j):
   ice = defaultdict(int)
   queue = deque()
   queue.append([i, j])
   while queue:
      i, j = queue.popleft()
      for k in range(4):
         nx = i + dx[i]
         ny = i + dy[i]
         if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
               ice[(x, y)] += 1
            elif graph[nx][ny] != 0 and check[nx][ny]:
               check[nx][ny] = 0
               queue.append([nx, ny])


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

year = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while True:
   check = [[1 for _ in range(n)] for _ in range(m)]
   cnt = 0
   for i in range(n):
      for j in range(m):
         if graph[i][j] != 0 and check[i][j]:
            check[i][j] = 0
            ice = bfs(i, j)
            cnt += 1
      
   if cnt > 1:
      print(year)
      break
   if cnt == 0:
      print(0)
      break

   for (x, y), melting in ice.items():
      graph[x][y] = 0 if graph[x][y] < melting else graph[x][y] - cnt
   year += 1