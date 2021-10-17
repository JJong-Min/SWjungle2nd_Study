import sys

N = int(sys.stdin.readline().strip())
check_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
check_dist = 0
total_sum = 0

for i in range(N - 1):
    total_sum += abs(check_list[i][0] - check_list[i + 1][0]) + abs(check_list[i][1] - check_list[i + 1][1])

for i in range(1, N - 1):
    left_dist = abs(check_list[i - 1][0] - check_list[i][0]) + abs(check_list[i - 1][1] - check_list[i][1])
    right_dist = abs(check_list[i + 1][0] - check_list[i][0]) + abs(check_list[i + 1][1] - check_list[i][1])
    skip_dist = abs(check_list[i + 1][0] - check_list[i - 1][0]) + abs(check_list[i + 1][1] - check_list[i - 1][1])
    sub_dist = left_dist + right_dist - skip_dist
    check_dist = max(check_dist, sub_dist)

print(total_sum - check_dist)

'''
import sys
from itertools import permutations, combinations

#print(list(combinations(arr, 2)))


def md(point1, point2):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    return abs(x1 - x2) + abs(y1 - y2)

n = int(sys.stdin.readline())
check_points = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]

dp[1][2] = md(check_points[0], check_points[1])
dp[1][3] = md(check_points[0], check_points[2])

for i in range(1, len(check_points) - 1):
    print(i)
    point1 = check_points[i]
    point2 = check_points[i + 1]
    dp[i + 1][i + 2] = min(dp[i][i + 1], dp[i - 1][i + 1]) + md(point1, point2)

    if i == len(check_points) - 2:
        break
    
    point2 = check_points[i + 2]
    dp[i + 1][i + 3] = dp[i][i + 1] + md(point1, point2)
    
print(min(dp[n - 2][n], dp[n - 1][n]))


last_distance1 = md(check_points[n - 2], check_points[n])
before_point = check_points[1]
distance = 0

if n > 3:
    for i in range(2, n - 1):
        distance += md(before_point, check_points[i])
        before_point = check_points[i]

last_distance1 += distance

last_distance2 = md(check_points[n - 1], check_points[n])
if n == 3:
    last_distance2 += md(check_points[1], check_points[2])
elif n == 4:
    last_distance2 += md(check_points[1], check_points[3])
else:
    new_check_points = [i for i in range(2, n - 1)]
    _comb = list(combinations(new_check_points, len(new_check_points) - 1))
    distance = 0
    before_point = check_points[1]
    for comb in _comb:
        distance += md(before_point, check_points[comb])
        before_point = check_points[comb]
    last_distance2 += distance

print(min(last_distance1, last_distance2))
