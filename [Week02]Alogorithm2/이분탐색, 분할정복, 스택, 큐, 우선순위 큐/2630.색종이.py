import sys

def check_color(x, y, n):
    global white_cnt, blue_cnt
    standard_color = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if standard_color != graph[i][j]:
                check_color(x, y, n//2)
                check_color(x, y + n//2, n//2)
                check_color(x + n//2, y, n//2)
                check_color(x + n//2, y + n//2, n//2)
                return

    if standard_color == 0:
        white_cnt += 1
        return
    else:
        blue_cnt += 1
        return
    
N = int(sys.stdin.readline())
graph = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

white_cnt = 0
blue_cnt = 0

check_color(0, 0, N)
print(white_cnt)
print(blue_cnt)
