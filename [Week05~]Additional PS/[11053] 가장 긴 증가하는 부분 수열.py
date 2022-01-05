import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
