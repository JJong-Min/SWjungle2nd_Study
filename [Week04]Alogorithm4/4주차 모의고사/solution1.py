import sys

n = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(n)]
dp = [[0 for _ in range(2)] for _ in range(n)]

if n == 1:
    print(stairs[0])
else:
    dp[0][0] = stairs[0]
    dp[1][0], dp[1][1] = stairs[1], stairs[1] + stairs[0]

    for i in range(2, n):
        dp[i][0] = max(dp[i - 2][0], dp[i - 2][1]) + stairs[i]
        dp[i][1] = dp[i - 1][0] + stairs[i]

    print(max(dp[n - 1][0], dp[n - 1][1])) 