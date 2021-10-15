from itertools import permutations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i  - 1]:
                continue
                
            total_sum = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if total_sum + nums[left] + nums[right] < 0:
                    left += 1
                elif total_sum + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return answer
                        
                    
        '''
        answer = set()
        nums_pers = permutations(nums, 3)
        for nums_per in nums_pers:
            if sum(nums_per) == 0:
                nums_per = sorted(list(nums_per))
                answer.add(tuple(nums_per))
        
        return answer
        '''
