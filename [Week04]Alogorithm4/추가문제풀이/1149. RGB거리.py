import sys

n = int(sys.stdin.readline())
RGB_val = [[0, 0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    
    
    for j in range(3):
        if j == 2:
            dp[i][j] = min(dp[i-1][j-1] + RGB_val[i][j], dp[i-1][j-2] + RGB_val[i][j])
        elif j == 0:
            dp[i][j] = min(dp[i-1][j+1] + RGB_val[i][j], dp[i-1][j+2] + RGB_val[i][j])
        else:
            dp[i][j] = min(dp[i-1][j+1] + RGB_val[i][j], dp[i-1][j-1] + RGB_val[i][j])
    
print(min(dp[n]))
