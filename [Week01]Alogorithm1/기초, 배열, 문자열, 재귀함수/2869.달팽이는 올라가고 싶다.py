import sys
# 내 풀이
A, B, V = map(int, (sys.stdin.readline().split()))
before_last_day_height = V - A
days = 1

if before_last_day_height % (A - B) == 0:
    days += before_last_day_height // (A - B)

else:
    days += before_last_day_height // (A - B) + 1

# 다른 사람 풀이
#if -else가 아닌 math.ceil을 사용

import math
A, B, V = map(int, input().split())
# print(A, B, V)
day_count = (V - B) / (A - B)
print(math.ceil(day_count))