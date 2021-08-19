import sys

def check(x, y, n):
    if n == 1:
        return True

    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[x][y] != graph[i][j]:
                return False

    return True
            

def solution(x, y, n):
    if check(x, y, n):
        print(graph[x][y], end="")
        return
    
    print("(", end="")
    solution(x, y, n // 2)
    solution(x, y + n // 2, n // 2)
    solution(x + n // 2, y, n // 2)
    solution(x + n // 2, y + n // 2, n // 2)
    print(")", end="")
    return


N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

solution(0, 0, N)
