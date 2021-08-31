import sys

n = int(sys.stdin.readline())
num_arr = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(n)]
for i in range(1, len(num_arr)):
    for j in range(i):
        if num_arr[i] > num_arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
