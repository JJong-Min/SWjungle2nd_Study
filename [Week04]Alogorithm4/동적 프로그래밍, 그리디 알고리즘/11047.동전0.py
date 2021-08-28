
import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
coins.sort(reverse=True)

ans = 0
for coin in coins:
    if k // coin > 0:
        ans += k // coin
        k %= coin

print(ans)
