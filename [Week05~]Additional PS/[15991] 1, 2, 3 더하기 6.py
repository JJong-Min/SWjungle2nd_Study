import sys

t = int(sys.stdin.readline())
max_num = 100000
dp = [0, 1, 2, 2, 3, 3, 6] + [0] * (max_num - 6)
for i in range(7, max_num + 1):
    dp[i] = (dp[i - 2] + dp[i - 4] + dp[i - 6]) % 1000000009

for _ in range(t):
    n = int(sys.stdin.readline())

    print(dp[n])

