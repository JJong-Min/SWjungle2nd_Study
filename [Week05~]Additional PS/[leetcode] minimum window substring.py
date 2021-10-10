
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0
        for right, v in enumerate(s, 1):
            missing -= need[v] > 0
            need[v] -= 1
            
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                if not end or right - left <= end - start:
                    start, end = left, right
                
                need[s[left]] += 1
                missing += 1
                left += 1
        
        return s[start:end]
    
        # 시간초과
        '''
        def contains(s_substr_lst: List, t_lst: List):
            for t_elem in t_lst:
                if t_elem in s_substr_lst:
                    s_substr_lst.remove(t_elem)
                else:
                    return False
            
            return True
        
        if not s or not t:
            return ''
        
        window_size = len(t)
        
        for size in range(window_size, len(s) + 1):
            for left in range(len(s) - size + 1):
                s_substr = s[left:left + size]
                if contains(list(s_substr), list(t)):
                    return s_substr
        return ''
        '''
    
        # t가 중복되지 않는다는 조건 하에 푼 풀이
        '''
        k = len(t)
        while k <= len(s):
            for i in range(len(s) - k + 1):
                _sub = s[i:i+k]
                for i in t:
                    if i not in _sub:
                        break
                else:
                    return _sub
            k += 1
        return ""
        '''
