import sys

n = int(sys.stdin.readline())
conferences = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
conferences.sort()
conferences.sort(key=lambda x: x[1])

last_time = 0
cnt = 0

for start, end in conferences:
    if last_time <= start:
        last_time = end
        cnt += 1

print(cnt)

'''
# 틀린 풀이
import sys

n = int(sys.stdin.readline())

conferences = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
conferences.sort()

available_con = []
gap = 100000
cnt = 0
for conference in conferences:
    if not available_con:
        gap = conference[1] - conference[0]
        available_con.append(conference)
    else:
        if available_con[cnt][1] <= conference[0]:
            cnt += 1

        elif gap > conference[1] - conference[0]:
            available_con.pop()

        else:
            continue

        gap = conference[1] - conference[0]
        available_con.append(conference)

print(cnt + 1)
 '''       
