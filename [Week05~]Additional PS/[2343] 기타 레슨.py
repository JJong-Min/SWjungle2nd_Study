import sys

n, m = map(int, sys.stdin.readline().split())
lecture_times = list(map(int, sys.stdin.readline().split()))
start = max(lecture_times)
end = sum(lecture_times)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    sum_time = 0
    for i in range(len(lecture_times)):
        if sum_time + lecture_times[i] > mid:
            cnt += 1
            sum_time = 0
        sum_time += lecture_times[i]

    if sum_time > 0:
        cnt += 1

    if cnt > m:
        start = mid + 1

    else:
        ans = mid
        end = mid - 1

print(ans)
        
