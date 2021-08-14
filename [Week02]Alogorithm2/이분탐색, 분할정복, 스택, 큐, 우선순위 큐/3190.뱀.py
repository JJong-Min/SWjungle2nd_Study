import sys
from collections import deque

def rotation_direction(x, y):
    if x == 'L':
        if y == 'L':
            return 'D'
        else:
            return 'U'

    elif x == 'R':
        if y == 'L':
            return 'U'
        else:
            return 'D'

    elif x == 'U':
        if y == 'L':
            return 'L'
        else:
            return 'R'

    else:
        if y == 'L':
            return 'R'
        else:
            return 'L'

N = int(sys.stdin.readline())
graph = [[0 for _ in range(N)] for _ in range(N)]

K = int(sys.stdin.readline())
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    graph[x - 1][y - 1] = 1

change_directions = {}
L  = int(sys.stdin.readline())
for _ in range(L):
    seconds, direction = sys.stdin.readline().split()
    change_directions[seconds] = direction

go_to = {'L' : (0, -1), 'R' : (0, 1), 'U' : (-1, 0), 'D' : (1, 0)}


start_point = (0, 0, 'R')
graph[0][0] = 2
snake_length = deque([(0, 0)])
queue = deque([start_point])
cnt = 0

while queue:
    cnt += 1
    x, y, direction = queue.popleft()
    dx, dy = go_to[direction]
    nx, ny = x + dx, y + dy
    if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1 or graph[nx][ny] == 2:
        break
    else:
        if graph[nx][ny] != 1:
            tail_x, tail_y = snake_length.popleft()
            graph[tail_x][tail_y] = 0

        if str(cnt) in change_directions.keys():
            direction = rotation_direction(direction, change_directions[str(cnt)])
            
        snake_length.append((nx, ny))
        graph[nx][ny] = 2
        queue.append([nx, ny, direction])            

print(cnt)
