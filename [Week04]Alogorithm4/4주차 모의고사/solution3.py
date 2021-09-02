import sys

n, k = map(int, sys.stdin.readline().split())
products = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(k)]

remove_products = []
ans = 0

for i in range(k):
    for idx in remove_products:
        del products[idx]
    dp = [[0 for _ in range(k + 1)] for _ in range(len(products) + 1)]
    for q in range(1, len(products) + 1):
        for p in range(1, k + 1):
            if products[q][0] > p:
                dp[q][p] = dp[q - 1][p]
            else:
                