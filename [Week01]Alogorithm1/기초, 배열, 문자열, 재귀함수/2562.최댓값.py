import sys

order = 0
max_num = 0

for i in range(1, 10):
    num = int(sys.stdin.readline())
    if num > max_num:
        order = i
        max_num = num

print(max_num)
print(order)
