import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(sys.stdin.readline().rstrip())
stack = []

for num in nums:
    if stack and k > 0 and int(stack[-1]) < int(num):
        while (stack and k > 0 and int(stack[-1]) < int(num)):
            stack.pop()
            k -= 1
    stack.append(num)

while k > 0:
    min_num = min(stack)
    stack.remove(min_num)
    k -= 1

print(''.join(stack))
