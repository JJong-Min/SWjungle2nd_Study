import sys
from collections import deque

d, teacher_word = sys.stdin.readline().rstrip().split()
dictionary_words = [sys.stdin.readline().rstrip() for _ in range(int(d))]
ans = ''

def check_word(now_word):
    next_words = []

    for word in dictionary_words:
        if len(now_word) + 1 != len(word):
            continue

        if now_word in word:
            next_words.append(word)
            continue

        now_word_idx = 0
        word_idx = 0
        while word_idx < len(word):
            if now_word[now_word_idx] == word[word_idx]:
                now_word_idx += 1
            word_idx += 1

        if now_word_idx == len(now_word):
            next_words.append(word)
        
    return next_words




def bfs(first_word):
    queue = deque([first_word])

    while queue:
        global ans
        now_word = queue.popleft()
        if len(now_word) > len(ans):
            ans = now_word

        next_words = check_word(now_word)
        queue.extend(next_words)

    return

bfs(teacher_word)
print(ans)
