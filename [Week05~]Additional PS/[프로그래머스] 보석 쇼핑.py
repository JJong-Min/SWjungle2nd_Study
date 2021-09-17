# 풀이1(시간초과)
def solution(gems):
    gems_kinds = len(set(gems))
    lp = 0
    min_len = float('INF')
    start = 0
    end = 0
    while lp < len(gems):
        for rp in range(lp, len(gems)):
            if rp - lp >= min_len:
                break
            now_gems_kinds = len(set(gems[lp:rp + 1]))
            if gems_kinds == now_gems_kinds and rp - lp < min_len:
                min_len = rp - lp
                start = lp
                end = rp
                break
        lp += 1
    answer = [start + 1, end + 1]
    return answer      


# 풀이 2 (딕셔너리 활용)
from collections import defaultdict

def solution(gems):
    gdict = defaultdict(int)
    gnum = len(set(gems))
    
    left = 0
    right = 0
    answer = [1, len(gems)]
    while right < len(gems):
        gdict[gems[right]] += 1
        right += 1
        
        if len(gdict) == gnum:
            while left < right:
                if gdict[gems[left]] <= 1:
                    break
                gdict[gems[left]] -= 1
                left += 1
            
            if answer[1] + 1 - answer[0] > right - left:
                answer = [left + 1, right]
    return answer  
