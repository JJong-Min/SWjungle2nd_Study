import sys

n = int(sys.stdin.readline())
dp = [[0 for _ in range(6)] for _ in range(n + 1)]
cnt = 0
grade = 0
for i in range(1, n + 1):
    a, b = map(int, sys.stdin.readline().split())
    dp[i][a] = dp[i - 1][a] + 1

#    if cnt == dp[i][a]:
#       grade = min(grade, a)
    if cnt < dp[i][a]:
        cnt = dp[i][a]
        grade = a

    if a != b:
        dp[i][b] = dp[i - 1][b] + 1
       # if cnt == dp[i][a]:
        #    grade = min(grade, b)
        if cnt < dp[i][b]:
            cnt = dp[i][b]
            grade = b

print(cnt, grade)
