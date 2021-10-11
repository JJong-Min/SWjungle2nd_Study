class Solution:
    def isPalindrome(self, s: str) -> bool:
        list_s = [i.upper() for i in s if i.isalnum()]
        mid = len(list_s) // 2
        
        if len(list_s) % 2 == 1:
            left_s = list_s[:mid]
            right_s = list_s[mid + 1:]
        
        else:
            left_s = list_s[:mid]
            right_s = list_s[mid:]
        
        if left_s == right_s[::-1]:
            return True
        else:
            return False


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True
                
