from collections import deque

def check(word1, word2):
    different_cnt = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            different_cnt += 1
    
    if different_cnt == 1:
        return True
    return False

def solution(begin, target, words):
    answer = 0
    queue = deque([(begin, 0)])
    
    if target not in words:
        return 0
    
    while queue:
        now_word, cnt = queue.popleft()
        if now_word == target:
            return cnt
        
        for word in words:
            if check(now_word, word):
                queue.append((word, cnt + 1))
        
    return answer
