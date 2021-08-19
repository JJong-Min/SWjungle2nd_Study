import sys

def solution(x, y, n):
    global zero_cnt, minus_cnt, plus_cnt
    standard_num = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if standard_num != graph[i][j]:
                solution(x, y, n//3)
                solution(x, y + n//3, n//3)
                solution(x, y + 2 * (n // 3), n//3)
                solution(x + n // 3, y, n//3)
                solution(x + 2 * (n // 3), y, n//3)
                solution(x + n // 3, y + n // 3, n//3)
                solution(x + 2 * (n // 3), y + n // 3, n//3)
                solution(x + n // 3, y + 2 * (n // 3), n//3)
                solution(x + 2 * (n // 3), y + 2 * (n // 3), n//3)
                return

    if standard_num == 0:
        zero_cnt += 1
        return
    elif standard_num == 1:
        plus_cnt += 1
        return
    else:
        minus_cnt += 1
        return
    
N = int(sys.stdin.readline())
graph = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

zero_cnt = 0
minus_cnt = 0
plus_cnt = 0
solution(0, 0, N)
print(minus_cnt)
print(zero_cnt)
print(plus_cnt)
