import sys
from collections import deque

word = sys.stdin.readline().rstrip()

double_alphabet = set({"d", "l", "n"})
single_alphabet = set({"c", "s", "z"})
answer = 0

queue = deque(list(word))
while queue:
    alphabet = queue.popleft()

    if alphabet in single_alphabet:
        if len(queue) > 0 and (queue[0] == '=' or queue[0] == '-'):
            queue.popleft()
            
    elif alphabet in double_alphabet:
        if alphabet == 'd':
            if len(queue) > 1 and queue[0] == 'z' and queue[1] == '=':
                queue.popleft()
                queue.popleft()
            elif len(queue) > 0 and queue[0] == '-':
                queue.popleft()
        elif len(queue) > 0 and queue[0] == 'j':
            queue.popleft()

    answer += 1
print(answer)

    

T = input()
dics = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for key in dics:
    T = T.replace(key, "_")
print(len(T))
