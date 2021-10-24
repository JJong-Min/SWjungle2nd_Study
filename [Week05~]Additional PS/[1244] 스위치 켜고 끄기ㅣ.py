import sys

n = int(sys.stdin.readline())
switchs = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
for _ in range(m):
    gender, num = map(int, sys.stdin.readline().split())
    if gender == 1:
        change_switch_nums = [i for i in range(num, n + 1) if i % num == 0]
        for switch_num in change_switch_nums:
            switchs[switch_num - 1] = not switchs[switch_num - 1]


    else:
        num -= 1
        switchs[num] = not switchs[num]
        expand_num = 1
        while True:
            left_num =num - expand_num
            right_num = num + expand_num

            if left_num < 0 or right_num > n - 1 or switchs[left_num] != switchs[right_num]:
                break
            switchs[left_num] = not switchs[left_num]
            switchs[right_num] = not switchs[right_num]
            expand_num += 1

switchs = [1 if i else 0 for i in switchs]

for i, switch in enumerate(switchs):
    if i % 20 == 19:
        print(switch)
    else:
        print(switch, end = ' ')
