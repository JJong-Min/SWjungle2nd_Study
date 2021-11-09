import sys

strings = sys.stdin.readline().rstrip()
bomb_string = sys.stdin.readline().rstrip()
stack = []

for char in strings:
    stack.append(char)
    if stack[-1] == bomb_string[-1] and ''.join(stack[-len(bomb_string):]) == bomb_string:
        del stack[-len(bomb_string):]

answer = ''.join(stack)
if answer:
    print(answer)
else:
    print('FRULA')
                    
        
'''
import sys

strings = sys.stdin.readline().rstrip()
bomb_string = sys.stdin.readline().rstrip()
left = 0
right = left + len(bomb_string)

while right <= len(strings) and strings != '':
    if strings[left:right] == bomb_string:
        while strings[left:right] == bomb_string:
            strings = strings[:left] + strings[right:]
            left -= 1
            right = left + len(bomb_string)
    else:
        left += 1
        right = left + len(bomb_string)

if strings == '':
    print('FRULA')
else:
    print(strings)
'''
