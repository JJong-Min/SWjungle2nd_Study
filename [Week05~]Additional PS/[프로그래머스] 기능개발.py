import math

def solution(progresses, speeds):
    before_distribution_day = 0
    success_working_cnt = 0
    answer = []
    for progress, speed in zip(progresses, speeds):
        remain_working = 100 - progress
        distribution_day = math.ceil(remain_working / speed)
        if before_distribution_day == 0:
            before_distribution_day = distribution_day
            success_working_cnt = 1
        elif before_distribution_day >= distribution_day:
            success_working_cnt += 1
        else:
            before_distribution_day = distribution_day
            answer.append(success_working_cnt)
            success_working_cnt = 1
    answer.append(success_working_cnt)
    return answer
