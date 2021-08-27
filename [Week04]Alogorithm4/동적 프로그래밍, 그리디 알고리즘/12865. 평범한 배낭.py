import sys

n, k = map(int, sys.stdin.readline().split())
things = [[0, 0]]
for _ in range(n):
        things.append(list(map(int, sys.stdin.readline().split())))
        
                           

matrix = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = things[i][0]
        value = things[i][1]
        
        if things[i][0] <= j:
           matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - weight] + value)
        else:
            matrix[i][j] = matrix[i - 1][j]
    
print(matrix[n][k])

# 틀렸습니다 코드
import sys

n, k = map(int, sys.stdin.readline().split())
things = [(0, 0)]
for _ in range(n):
    w, k = map(int, sys.stdin.readline().split())
    things.append((w, k))

matrix = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = things[i][0]
        value = things[i][1]
        
        if things[i][0] <= j:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - weight] + value)
        else:
            matrix[i][j] = matrix[i - 1][j]
    
print(matrix[n][k])
