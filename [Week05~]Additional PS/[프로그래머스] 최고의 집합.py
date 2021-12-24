def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    
    if n == 1:
        return [s]
    
    answer = [s // n] * n
    if s % n == 0:
        return answer
    
    else:
        remainder = s % n
        for i in range(remainder):
            answer[(-1) - i] += 1
    
    return answer
