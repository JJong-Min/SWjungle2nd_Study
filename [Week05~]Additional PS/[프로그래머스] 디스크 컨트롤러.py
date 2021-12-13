'''
import heapq, math
from collections import deque

def solution(jobs):
    total_working_time = 0
    total_job_cnt = len(jobs)
    if total_job_cnt == 1:
        return jobs[0][1] + jobs[0][0]
    
    jobs = deque(sorted(jobs))
    first_job_request_time, first_job_working_time = jobs.popleft()
    total_working_time += (first_job_working_time + first_job_request_time)
    now_time = first_job_working_time + first_job_request_time
    
    heap = []
    for job in jobs:
        job_request_time = job[0]
        job_working_time = job[1]
        if job_request_time <= now_time:
            heapq.heappush(heap, (job_working_time, job_request_time))
        
        else:
            while now_time < job_request_time:
                now_job_working_time, now_job_request_time = heapq.heappop(heap)
                total_working_time += now_job_working_time
                total_working_time += (now_time - now_job_request_time)
                now_time += now_job_working_time
            heapq.heappush(heap, (job_working_time, job_request_time))
        
    while heap:
        now_job_working_time, now_job_request_time = heapq.heappop(heap)
        total_working_time += now_job_working_time
        total_working_time += (now_time - now_job_request_time)
        now_time += now_job_working_time
        
    answer = math.floor(total_working_time / total_job_cnt)
    return answer
'''

import heapq

def solution(jobs):
    answer, now , i = 0, 0, 0
    start = -1
    heap = []
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, (job[1], job[0]))
            
        if heap:
            curr = heapq.heappop(heap)
            start = now
            now += curr[0]
            answer += now - curr[1]
            i += 1
        
        else:
            now += 1
    
    
    return answer // len(jobs)
