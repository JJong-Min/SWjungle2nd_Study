
import sys

expression = sys.stdin.readline().rstrip().split('-')

for i in range(len(expression)):
    if '+' in expression[i]:
        expression[i] = sum([int(i) for i in  expression[i].split('+')])
    else:
        expression[i] = int(expression[i])

ans = expression[0]

for i in range(1, len(expression)):
    ans -= expression[i]

print(ans)

'''
# syntaxError
import sys

expression = sys.stdin.readline().rstrip().split('-')

for i in range(len(expression)):
    expression[i] = eval(expression[i])

ans = expression[0]

for i in range(1, len(expression)):
    ans -= expression[i]

print(ans)
'''
