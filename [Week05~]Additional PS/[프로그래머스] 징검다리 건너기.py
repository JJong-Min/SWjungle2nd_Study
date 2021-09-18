def solution(stones, k):
    left_pointer = 1
    right_pointer = max(stones)
    answer = 0
    
    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer) // 2
        zero_cnt = 0
        for stone in stones:
            if stone - mid <= 0:
                zero_cnt += 1
            else:
                zero_cnt = 0

            if zero_cnt >= k:
                right_pointer = mid - 1
                break
        
        else:
            answer = mid + 1
            left_pointer = mid + 1
        
    return answer
