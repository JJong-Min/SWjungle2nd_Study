import sys

n, m = map(int, sys.stdin.readline().split())
lecture_times = list(map(int, sys.stdin.readline().split()))

left = max(lecture_times)
right = sum(lecture_times)
answer = sum(lecture_times)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    sum_time = 0
    for i in range(n):
        if sum_time + lecture_times[i] > mid:
            cnt += 1
            sum_time = 0
        sum_time += lecture_times[i]

    if sum_time > 0:
        cnt += 1

    if cnt > m:
        left = mid + 1

    else:
        answer = mid
        right = mid - 1

print(answer)
