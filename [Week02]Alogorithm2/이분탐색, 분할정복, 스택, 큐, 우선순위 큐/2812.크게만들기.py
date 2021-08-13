# 정상 동작
import sys

N, K = map(int, sys.stdin.readline().split())
nums = sys.stdin.readline().rstrip()
stack = []

for num in nums:
    if stack == []:
        stack.append(num)
    else:
        if K > 0 and int(stack[-1]) < int(num):
            while (stack and int(stack[-1]) < int(num) and K > 0):
                stack.pop()
                K -= 1
        stack.append(num)

            
while K > 0:
    min_num = min(stack)
    stack.remove(min_num)
    K -= 1
print(''.join(stack))
