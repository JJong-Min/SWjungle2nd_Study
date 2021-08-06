import sys

T = int(sys.stdin.readline())
for _ in range(T):
    repeat_num, chars = sys.stdin.readline().rstrip().split()
    repeat_num = int(repeat_num)
    answer = ''

    for char in chars:
        answer += char*repeat_num

    print(answer)