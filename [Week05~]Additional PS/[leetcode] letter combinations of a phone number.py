class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            
            for i in range(index, len(digits)):
                for j in num_dict[digits[i]]:
                    dfs(i + 1, path + j)
                
        result = []
        num_dict = {'2': ['a', 'b', 'c'], '3':['d','e','f'], '4':['g','h','i'], '5': ['j', 'k', 'l'], '6':['m','n','o'], '7':['p', 'q', 'r'], '8':['s','t','u'], '9':['w','x','y','z']}
        if digits == '':
            return result
        
        dfs(0, "")
        return result
