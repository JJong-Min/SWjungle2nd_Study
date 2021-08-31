import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))
