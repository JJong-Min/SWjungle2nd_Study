import sys

while True:
    input_vals = list(map(int, sys.stdin.readline().split()))
    n = input_vals[0]
    heights = input_vals[1:]

    if n == 0:
        break
    else:
        stack = []
        ans = 0
        for i in range(n):
            if not stack:
                stack.append([heights[i], i])

            elif stack[-1][0] >= heights[i]:
                while stack and stack[-1][0] >= heights[i]:
                    h, idx = stack.pop()
                    ans = max(ans, h * (i - idx))

                stack.append([heights[i], idx])

            else:
                stack.append([heights[i], i])



        while stack:
            h, idx = stack.pop()
            ans = max(ans, h * (n - idx))

    print(ans)

        
        
