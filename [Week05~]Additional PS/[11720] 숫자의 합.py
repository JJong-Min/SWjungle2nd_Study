import sys

n = int(sys.stdin.readline())
number = list(sys.stdin.readline().rstrip())
print(sum([int(i) for i in number]))
