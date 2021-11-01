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
