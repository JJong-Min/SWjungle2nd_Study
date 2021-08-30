import sys
import copy
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = copy.deepcopy(arr)

for i in range(1, n):
    dp[i] = max(dp[i], dp[i] + arr[i - 1], dp[i - 1] + arr[i])

print(max(dp))
        
    
    
