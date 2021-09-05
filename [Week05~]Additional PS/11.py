# 정답
import sys
n = int(sys.stdin.readline())
consults = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp_table = [0] * (n + 1)

for i in range(n):
    if i + consults[i][0] <= n:
        dp_table[i + consults[i][0]] = max(dp_table[i + consults[i][0]], consults[i][1] + dp_table[i])
    dp_table[i + 1] = max(dp_table[i + 1], dp_table[i])
print(dp_table[n])

# 시간초과
import sys

n = int(sys.stdin.readline())
consults = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp_table = [consults[0][1]] + [0] * (n - 1)

for i in range(1, n):
    if i + consults[i][0] > n:
        dp_table[i] = dp_table[i - 1]
        continue
    for j in range(i):
        if i - j >= consults[j][0]:
            dp_table[i] = max(dp_table[i], consults[i][1] + dp_table[j])
        
    if dp_table[i] == 0:
        dp_table[i] = consults[i][1]

print(max(dp_table))
