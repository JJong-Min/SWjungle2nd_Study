import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0 for _ in range(n)] for _ in range(n)]
m_position = ()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = n // 2, n // 2
num = 1
graph[x][y] = num
length = 0

while True:
    for i in range(4):
        for _ in range(length):
            num += 1
            x += dx[i]
            y += dy[i]
            graph[x][y] = num
            if num == m:
                m_position = (x + 1, y + 1)
    
    if x == 0 and y == 0:
        break
   
    x -= 1
    y -= 1
    length += 2

for i in range(n):
    print(*graph[i])
print(*m_position)



import copy
n = int(input())
m = int(input())
snail = []
temp = []
for i in range(n):
    temp.append(0)
for i in range(n):
    snail.append(copy.deepcopy(temp))
    
move = [[0,1],[1,0],[0,-1],[-1,0]]
d = 0
now_x = 0 ; now_y = 0 ; now_num = n*n
while(now_num > 0):
    snail[now_y][now_x] = now_num
    if(now_x + move[d][0] < 0 or now_x + move[d][0] >= n or now_y + move[d][1] < 0 or now_y + move[d][1] >= n or snail[now_y+move[d][1]][now_x+move[d][0]] != 0):
        d = (d + 1) % 4
    now_y = now_y + move[d][1]
    now_x = now_x + move[d][0]
    now_num = now_num - 1
for i in range(n):
    for j in range(n):
        if(snail[i][j] == m):
            find_x = j
            find_y = i
        print(snail[i][j] , end = ' ')
    print()
print(find_y + 1,find_x + 1)
