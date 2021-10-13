class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return i, nums_map[target - num]
        '''
        for i, n in enumerate(nums):
            _n = target - n
            if _n in nums[i + 1:]:
                return i, nums[i + 1:].index(_n) + i + 1
        '''
        '''
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        '''
