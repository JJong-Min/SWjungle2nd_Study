class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_element = []
        
        def dfs(element):
            if len(element) == 0:
                result.append(prev_element[:])
            
            for e in element:
                next_element = element[:]
                next_element.remove(e)
                
                prev_element.append(e)
                dfs(next_element)
                prev_element.pop()
        
        dfs(nums)
        return result
