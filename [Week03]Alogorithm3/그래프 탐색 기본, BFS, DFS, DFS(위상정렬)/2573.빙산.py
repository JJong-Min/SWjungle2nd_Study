import sys
from collections import deque
'''
def bfs(i, j):
   queue = deque([[i, j]])
   dx = [1, -1, 0, 0]
   dy = [0, 0, 1, -1]
   while queue:
      x, y = queue.popleft()
      for i in range(4):
         nx = x + dx[i]
         ny = y + dy[i]
         if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] != 0:
               if check[nx][ny]:
                  check[nx][ny] = False
                  queue.append([nx, ny])
            else:
               if graph[x][y] > 0 and zero_check[nx][ny]:
                  graph[x][y] -= 1

   if graph[x][y] == 0:
      zero_check[x][y] = False

########입력 받기#########   
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]

for i in range(n):
   graph[i] = list(map(int, sys.stdin.readline().split()))
########################

######탐색#########
ans = 0
cnt = 0
while cnt < 2:
   check = [[True for _ in range(m)] for _ in range(n)]
   zero_check = [[True for _ in range(m)] for _ in range(n)]
   cnt = 0
   for i in range(n):
      for j in range(m):
         if graph[i][j] != 0 and check[i][j]:
            cnt += 1
            check[i][j] = False
            bfs(i, j)

   #####빙산이 다 녹은 경우 확인##########       
   flag = False        
   for i in range(n):
      for j in range(m):
         if graph[i][j] != 0:
            flag = True
            break
      if flag:
         ans += 1
         break
   else:
      print(0)
      exit(0)
         
         
print(ans)
'''


