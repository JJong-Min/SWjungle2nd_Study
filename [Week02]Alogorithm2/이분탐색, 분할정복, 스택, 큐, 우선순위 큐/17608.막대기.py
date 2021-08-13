import sys

N = int(sys.stdin.readline())
stack = []
num_arr = []
for _ in range(N):
    num_arr.append(int(sys.stdin.readline()))
num_arr.reverse()

for num in num_arr:
    if stack == []:
        stack.append(num)
    elif stack[-1] < num:
        stack.append(num)

print(len(stack))
        
