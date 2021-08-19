
import sys

sticks = sys.stdin.readline()
stack = []
stick_num = 0
ans = 0
for stick in sticks:
    if stick == ')':
        # 이 전값이 (이면 레이저를 의미하므로 stick갯수를 하나 빼줌
        if stack[-1] == '(':
            stick_num -= 1
            # 스틱 갯수가 0개가 아니면 지금까지 앞에 있던 stick갯수를 ans에 저장
            if stick_num != 0:
                ans += stick_num
            # 닫는 괄호도 스택에 쌓음
            # 스틱의 마지막을 의미하는지, 레이저를 의미하는지를 알기 위해서
            stack.append(')')
        else:
            # 이 전값이 )이면 스틱의 마지막을 뜻하므로 stick갯수를 빼주고 ans에 하나 더함
            stick_num -= 1
            ans += 1

    else:
        # (이면 무조건 stick 갯수를 +1
        stick_num += 1
        stack.append('(')


print(ans)
