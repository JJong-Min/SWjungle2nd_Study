# 모래 계산하는 함수
def recount(s_x, s_y, direction):
    global ans

    if s_y < 0:
        return
        
    # 3. a, out_sand
    total = 0  # a 구하기 위한 변수
    for dx, dy, z in direction:
        nx = s_x + dx
        ny = s_y + dy
        if z == 0:  # a(나머지)
            new_sand = sand[s_x][s_y] - total
        else:  # 비율
            new_sand = int(sand[s_x][s_y] * z)
            total += new_sand

        if 0 <= nx < N and 0 <= ny < N:  # 인덱스 범위이면 값 갱신
            sand[nx][ny] += new_sand
        else:  # 범위 밖이면 ans 카운트
            ans += new_sand


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]

# 2. 방향별 모래 비율 위치
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x,y,z in left]
down = [(-y, x, z) for x,y,z in left]
up = [(y, x, z) for x,y,z in left]

s_x, s_y = N//2, N//2
ans = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 1.토네이도 회전 방향(y위치)
dict = {0: left, 1: down, 2: right, 3: up}
time = 0
for i in range(2*N-1):
    # 몫: i//4(타임+1), 나머지:i%4(방향)
    d = i % 4
    if d == 0 or d == 2:  # 다음 회차(d==0) 이거나 right(d==2) 이면 한번 더
        time += 1
    for _ in range(time):
        n_x = s_x + dx[d]
        n_y = s_y + dy[d]
        recount(n_x, n_y, dict[d])  # y좌표, 방향
        s_x, s_y = n_x, n_y

print(ans)


import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
start = (n // 2, n // 2)
len_cnt = 0
# 아 왼 위 오
direction = [(1, 0), (0, -1), (-1, 0) , (0, 1)]
out_sand = 0

for count in range(2 * n - 1, 0, -1):
    
    dx, dy = direction[count % 4]
    dx *= (len_cnt // 2 + 1)
    dy *= (len_cnt // 2 + 1)
    nx = start[0] + dx
    ny = start[1] + dy
    if graph[nx][ny] == 0:
        start = (nx, ny)
        len_cnt += 1
        continue
    # 왼쪽 이동
    if count % 4 == 1:
        sand = graph[nx][ny]
        a_sand = graph[nx][ny]
        
        if 0 <= nx - 1 < n and 0 <= ny < n:
            graph[nx - 1][ny] += int(sand * 0.07)
        else:
            out_sand += int(sand * 0.07)
        a_sand -= int(sand * 0.07)
        
        if 0 <= nx + 1 < n and 0 <= ny < n:
            graph[nx + 1][ny] += int(sand * 0.07)
        else:
            out_sand += int(sand * 0.07)
        a_sand -= int(sand * 0.07)
    
        if 0 <= nx - 2 < n and 0 <= ny< n:
            graph[nx - 2][ny] += int(sand * 0.02)
        else:
            out_sand += int(sand * 0.02)
        a_sand -= int(sand * 0.02)
        
        if 0 <= nx + 2 < n and 0 <= ny - 0 < n:
            graph[nx + 2][ny] += int(sand * 0.02)
        else:
            out_sand += int(sand * 0.02)
        a_sand -= int(sand * 0.02)
        
        if 0 <= nx - 1 < n and 0 <= ny - 1 < n:
            graph[nx - 1][ny - 1] += int(sand * 0.1)
        else:
            out_sand += int(sand * 0.1)
        a_sand -= int(sand * 0.1)
        
        if 0 <= nx + 1 < n and 0 <= ny - 1 < n:
            graph[nx + 1][ny - 1] += int(sand * 0.1)
        else:
            out_sand += int(sand * 0.1)
        a_sand -= int(sand * 0.1)

        if 0 <= nx - 1 < n and 0 <= ny + 1 < n:
            graph[nx - 1][ny + 1] += int(sand * 0.01)
        else:
            out_sand += int(sand * 0.01)
        a_sand -= int(sand * 0.01)
        
        if 0 <= nx + 1 < n and 0 <= ny + 1 < n:
            graph[nx + 1][ny + 1] += int(sand * 0.01)
        else:
            out_sand += int(sand * 0.01)
        a_sand -= int(sand * 0.01)

        if 0 <= nx < n and 0 <= ny - 2 < n:
            graph[nx][ny - 2] += int(sand * 0.05)
        else:
            out_sand += int(sand * 0.05)
        a_sand -= int(sand * 0.05)

        if 0 <= nx < n and 0 <= ny - 1 < n:
            graph[nx][ny - 1] += a_sand
        else:
            out_sand += a_sand
        graph[nx][ny] = 0

    # 위쪽 이동
    elif count % 4 == 2:
        sand = graph[nx][ny]
        a_sand = graph[nx][ny]
        
        if 0 <= nx < n and 0 <= ny - 1 < n:
            graph[nx][ny - 1] += int(sand * 0.07)
        else:
            out_sand += int(sand * 0.07)
        a_sand -= int(sand * 0.07)

        if 0 <= nx< n and 0 <= ny + 1 < n:
            graph[nx][ny + 1] += int(sand * 0.07)
        else:
            out_sand += int(sand * 0.07)
        a_sand -= int(sand * 0.07)
    
        if 0 <= nx - 1 < n and 0 <= ny + 2 < n:
            graph[nx - 1][ny + 2] += int(sand * 0.02)
        else:
            out_sand += int(sand * 0.02)
        a_sand -= int(sand * 0.02)
        
        if 0 <= nx - 1 < n and 0 <= ny - 2 < n:
            graph[nx - 1][ny - 2] += int(sand * 0.02)
        else:
            out_sand += int(sand * 0.02)
        a_sand -= int(sand * 0.02)
        
        if 0 <= nx - 1 < n and 0 <= ny - 1 < n:
            graph[nx - 1][ny - 1] += int(sand * 0.1)
        else:
            out_sand += int(sand * 0.1)
        a_sand -= int(sand * 0.1)
        
        if 0 <= nx - 1 < n and 0 <= ny + 1 < n:
            graph[nx - 1][ny + 1] += int(sand * 0.1)
        else:
            out_sand += int(sand * 0.1)
        a_sand -= int(sand * 0.1)

        if 0 <= nx + 1 < n and 0 <= ny + 1 < n:
            graph[nx + 1][ny + 1] += int(sand * 0.01)
        else:
            out_sand += int(sand * 0.01)
        a_sand -= int(sand * 0.01)
        
        if 0 <= nx + 1 < n and 0 <= ny - 1 < n:
            graph[nx + 1][ny - 1] += int(sand * 0.01)
        else:
            out_sand += int(sand * 0.01)
        a_sand -= int(sand * 0.01)

        if 0 <= nx - 2 < n and 0 <= ny < n:
            graph[nx - 2][ny] += int(sand * 0.05)
        else:
            out_sand += int(sand * 0.05)
        a_sand -= int(sand * 0.05)

        if 0 <= nx - 1 < n and 0 <= ny < n:
            graph[nx - 1][ny] += a_sand
        else:
            out_sand += a_sand
        graph[nx][ny] = 0
        
    # 오른쪽 이동
    elif count % 4 == 1:
        sand = graph[nx][ny]
        a_sand = graph[nx][ny]
        
        if 0 <= nx - 1 < n and 0 <= ny < n:
            graph[nx -1][ny] += int(sand * 0.07)
        else:
            out_sand += int(sand * 0.07)
        a_sand -= int(sand * 0.07)
        
        if 0 <= nx + 1 < n and 0 <= ny< n:
            graph[nx + 1][ny] += int(sand * 0.07)
        else:
            out_sand += int(sand * 0.07)
        a_sand -= int(sand * 0.07)
    
        if 0 <= nx - 2 < n and 0 <= ny + 1 < n:
            graph[nx - 2][ny + 1] += int(sand * 0.02)
        else:
            out_sand += int(sand * 0.02)
        a_sand -= int(sand * 0.02)
        
        if 0 <= nx + 2 < n and 0 <= ny + 1 < n:
            graph[nx + 2][ny + 1] += int(sand * 0.02)
        else:
            out_sand += int(sand * 0.02)
        a_sand -= int(sand * 0.02)
        
        if 0 <= nx - 1 < n and 0 <= ny + 1 < n:
            graph[nx - 1][ny + 1] += int(sand * 0.1)
        else:
            out_sand += int(sand * 0.1)
        a_sand -= int(sand * 0.1)
        
        if 0 <= nx + 1 < n and 0 <= ny + 1 < n:
            graph[nx + 1][ny + 1] += int(sand * 0.1)
        else:
            out_sand += int(sand * 0.1)
        a_sand -= int(sand * 0.1)

        if 0 <= nx - 1 < n and 0 <= ny - 1 < n:
            graph[nx - 1][ny - 1] += int(sand * 0.01)
        else:
            out_sand += int(sand * 0.01)
        a_sand -= int(sand * 0.01)
        
        if 0 <= nx - 1 < n and 0 <= ny + 1 < n:
            graph[nx - 1][ny + 1] += int(sand * 0.01)
        else:
            out_sand += int(sand * 0.01)
        a_sand -= int(sand * 0.01)

        if 0 <= nx < n and 0 <= ny + 2 < n:
            graph[nx][ny + 2] += int(sand * 0.05)
        else:
            out_sand += int(sand * 0.05)
        a_sand -= int(sand * 0.05)

        if 0 <= nx < n and 0 <= ny + 1 < n:
            graph[nx][ny + 1] += a_sand
        else:
            out_sand += a_sand
        graph[nx][ny] = 0

    # 아래쪽 이동
    else:
        sand = graph[nx][ny]
        a_sand = graph[nx][ny]
        
        if 0 <= nx< n and 0 <= ny - 1 < n:
            graph[nx][ny - 1] += int(sand * 0.07)
        else:
            out_sand += int(sand * 0.07)
        a_sand -= int(sand * 0.07)
        
        if 0 <= nx < n and 0 <= ny + 1 < n:
            graph[nx][ny + 1] += int(sand * 0.07)
        else:
            out_sand += int(sand * 0.07)
        a_sand -= int(sand * 0.07)
    
        if 0 <= nx + 1 < n and 0 <= ny -2  < n:
            graph[nx + 1][ny - 2] += int(sand * 0.02)
        else:
            out_sand += int(sand * 0.02)
        a_sand -= int(sand * 0.02)
        
        if 0 <= nx + 1 < n and 0 <= ny + 2 < n:
            graph[nx + 1][ny + 2] += int(sand * 0.02)
        else:
            out_sand += int(sand * 0.02)
        a_sand -= int(sand * 0.02)
        
        if 0 <= nx + 1 < n and 0 <= ny - 1 < n:
            graph[nx + 1][ny - 1] += int(sand * 0.1)
        else:
            out_sand += int(sand * 0.1)
        a_sand -= int(sand * 0.1)
        
        if 0 <= nx + 1 < n and 0 <= ny + 1 < n:
            graph[nx + 1][ny + 1] += int(sand * 0.1)
        else:
            out_sand += int(sand * 0.1)
        a_sand -= int(sand * 0.1)

        if 0 <= nx - 1 < n and 0 <= ny - 1 < n:
            graph[nx - 1][ny - 1] += int(sand * 0.01)
        else:
            out_sand += round(sand * 0.01)
        a_sand -= int(sand * 0.01)
        
        if 0 <= nx - 1 < n and 0 <= ny + 1 < n:
            graph[nx - 1][ny + 1] += int(sand * 0.01)
        else:
            out_sand += round(sand * 0.01)
        a_sand -= int(sand * 0.01)

        if 0 <= nx + 2 < n and 0 <= ny < n:
            graph[nx + 2][ny] += round(sand * 0.05)
        else:
            out_sand += round(sand * 0.05)
        a_sand -= int(sand * 0.05)

        if 0 <= nx + 1 < n and 0 <= ny <n:
            graph[nx + 1][ny] += a_sand
        else:
            out_sand += a_sand
        graph[nx][ny] = 0
    len_cnt += 1
    start = (nx, ny)
print(out_sand)
