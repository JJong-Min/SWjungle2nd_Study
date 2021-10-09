def solution(n, t, m, timetable):
    answer = 0
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()
    shuttle_time = [(9 * 60) + (t * i) for i in range(n)]
    
    i = 0
    for time in shuttle_time:
        cnt = 0
        while cnt < m and i < len(timetable) and timetable[i] <= time:
            i += 1
            cnt += 1
        
        if cnt < m:
            answer = time
        else:
            answer = timetable[i - 1] - 1
    answer = str(answer // 60).zfill(2) + ':' + str(answer % 60).zfill(2)
    return answer
