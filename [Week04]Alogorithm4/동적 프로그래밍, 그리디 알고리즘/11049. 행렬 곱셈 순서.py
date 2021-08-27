# dp (bottom up)
import sys

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp =[[0 for _ in range(N)] for _ in range(N)] 


for i in range(1, N):
    for j in range(0, N-i):
    
        if i == 1:
            dp[j][j+i] = matrix[j][0] * matrix[j][1] * matrix[j+i][1]
            continue
        
        dp[j][j+i] = 2**32
        for k in range(j, j+i): 
            dp[j][j+i] = min(dp[j][j+i], 
                             dp[j][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])
                
    
print(dp[0][N-1])


# 재귀 + dp (top down)
import sys

def count(a, b, c):
    return arr[a][0] * arr[b][1] * arr[c][1]

def mutiple(start, end):
    global dp
   
    if end == start:
        dp[start][end] = 0

    for i in range(end - start):
        if dp[start][start + i] == 999999999:
            mutiple(start, start + i)
        if dp[start + i + 1][end] == 999999999:
            mutiple(start + i + 1, end)
        dp[start][end] = min(dp[start][end], dp[start][start + i] + dp[start + i + 1][end] + count(start, start + i, end))

    return dp[start][end]

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a, b])
