import sys

n = int(sys.stdin.readline())
words = sys.stdin.readline().rstrip()
answer = 0
num = ''
for word in words:
    if word.isdigit():
        num += word
    else:
        if num:
            answer += int(num)
            num = ''

if num:
    answer += int(num)
print(answer)
