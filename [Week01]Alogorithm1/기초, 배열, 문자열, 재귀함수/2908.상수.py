import sys

num1, num2 = sys.stdin.readline().split()

num1 = num1[::-1]
num2 = num2[::-1]
print(max(int(num1), int(num2)))