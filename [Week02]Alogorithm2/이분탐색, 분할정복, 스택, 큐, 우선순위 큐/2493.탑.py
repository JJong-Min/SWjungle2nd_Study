# 정상 동작
import sys

N = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))
tops = [(i + 1, v) for i, v in enumerate(tops)]
stack = []

for top in tops:
    while stack:
        if stack[-1][1] <= top[1]:
            stack.pop()
        else:
            print(stack[-1][0], end = ' ')
            break

    if not stack:
        print(0, end = ' ')
    stack.append(top)



# 시간 초과
import sys

N = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))
tops = [(i + 1, v) for i, v in enumerate(tops)]
for i in range(N):
    stack = tops[:i]
    check = True
    while stack:
        if stack[-1][1] > tops[i][1]:
            print(stack[-1][0], end = ' ')
            check = False
            break
        else:
            stack.pop()

    if check:
        print(0, end = ' ')
