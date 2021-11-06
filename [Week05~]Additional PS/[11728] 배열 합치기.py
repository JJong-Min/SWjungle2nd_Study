import sys

n, m  = map(int, sys.stdin.readline().split())
a_arr = list(map(int, sys.stdin.readline().split()))
b_arr = list(map(int, sys.stdin.readline().split()))

new_arr = a_arr + b_arr
new_arr.sort()
print(*new_arr)
