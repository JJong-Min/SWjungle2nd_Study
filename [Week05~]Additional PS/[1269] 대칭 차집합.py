import sys

a_cnt, b_cnt = map(int, sys.stdin.readline().split())
a_arr = set(map(int, sys.stdin.readline().split()))
b_arr = set(map(int, sys.stdin.readline().split()))

print(len(a_arr - b_arr) + len(b_arr - a_arr))
