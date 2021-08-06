import sys

A, B, V = map(int, (sys.stdin.readline().split()))
before_last_day_height = V - A
days = 1

if before_last_day_height % (A - B) == 0:
    days += before_last_day_height // (A - B)

else:
    days += before_last_day_height // (A - B) + 1
