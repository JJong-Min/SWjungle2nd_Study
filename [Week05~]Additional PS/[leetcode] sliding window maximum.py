from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue
            
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v
            
            results.append(current_max)
            
            if current_max == window.popleft():
                current_max = float('-inf')
        
        return results
        '''
        # 시간초과 2
        for i in range(len(nums) - k + 1):
            answer.append(max(nums[i:i+k]))
        '''
        '''
        # 시간초과 1
        lp = 0
        while lp + k <= len(nums):
            new_nums = nums[lp:lp + k]
            lp += 1
        
        return answer
        '''
