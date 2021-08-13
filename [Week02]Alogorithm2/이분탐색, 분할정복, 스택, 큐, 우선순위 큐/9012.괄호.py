import sys

T = int(sys.stdin.readline())

for _ in range(T):
    stack = []
    gwalho = sys.stdin.readline().rstrip()
    flag = False
    for i in gwalho:
        if i == '(':
            stack.append(i)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = True
                break

    if stack or flag:
        print("NO")
    else:
        print("YES")
        
