class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t가 중복되지 않는다는 조건 하에 푼 풀이
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
