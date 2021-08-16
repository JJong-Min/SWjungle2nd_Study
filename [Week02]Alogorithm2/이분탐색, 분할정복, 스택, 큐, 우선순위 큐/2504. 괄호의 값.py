import sys

gwalhos = sys.stdin.readline().rstrip()
stack = []
ans = 0

for gwalho in gwalhos:
    if gwalho == ')':
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '(':
                if t == 0:
                    stack.append(2)
                else:
                    stack.append(2 * t)

                break

            elif top == '[':
                print(0)
                exit(0)
            else:
                t += int(top)

    elif gwalho == ']':
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '[':
                if t == 0:
                    stack.append(3)
                else:
                    stack.append(3 * t)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                t += int(top)

    else:
        stack.append(gwalho)
    print(stack)
for i in stack:
    if i =='(' or i == '[':
        print(0)
        exit(0)
    else:
        ans += i

print(ans)
