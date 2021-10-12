class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = collections.defaultdict(list)
        for str in strs:
            list_str = ''.join(sorted(list(str)))
            answer[list_str].append(str)
        
        return list(answer.values())
