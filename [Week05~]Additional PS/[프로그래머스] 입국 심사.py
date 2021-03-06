def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    
    while left < right:
        mid = (left + right) // 2
        people = 0
        
        for time in times:
            people += mid // time
        
        if people < n:
            left = mid + 1
            
        else:
            right = mid
    
    answer = left
    return answer
