import sys

n = int(sys.stdin.readline())
circles = []
for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    circles.append([x - r, 'L'])
    circles.append([x + r, 'R'])

circles.sort(key= lambda x: (-x[0], x[1]), reverse=True)

stack = []
ans = 1
for circle in circles:
    if circle[1] == 'L':
        stack.append(circle)

    else:
        cnt = 0
        while stack and stack[-1][1] != 'L':
            length, dummy = stack.pop()
            cnt += length

        length, dummy = stack.pop()
        if circle[0] - length == cnt:
            ans += 2
        else:
            ans += 1

        stack.append([circle[0] - length, 'C'])

print(ans)
