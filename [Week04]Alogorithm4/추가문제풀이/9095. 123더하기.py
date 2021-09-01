import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    dp = [0, 1, 2, 4] + [1 for _ in range(100000)]
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
                                     
    print(dp[n])                                
