from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)])
    while queue:
        number, idx = queue.popleft()
        if idx == len(numbers):
            if number == target:
                answer += 1
                
        else:
            queue.append((number + numbers[idx], idx + 1))
            queue.append((number - numbers[idx], idx + 1))
    
    return answer
