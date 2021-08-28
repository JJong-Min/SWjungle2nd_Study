# 


# 통과 bfs
import sys
from collections import deque

def bfs():
    queue = deque([[2, 1, 1]])

    while queue:
        point, jump, cnt = queue.popleft()
        
        for i in [jump, jump + 1, jump - 1]:
            if i > 0:
                next_point = point + i
                if next_point == n:
                    return cnt + 1
                if next_point < n and i not in check[next_point] and next_point not in impossible_jump_point:
                    check[next_point].append(i)
                    queue.append([next_point, i, cnt + 1])
        
    return -1

n, m = map(int, sys.stdin.readline().split())
check = [[] for _ in range(n + 1)]
impossible_jump_point = set()

for _ in range(m):
    idx = int(sys.stdin.readline())
    impossible_jump_point.add(idx)

print(bfs())


'''
# 시간 초과 (BFS)
import sys
from collections import deque

def bfs(num, jump, cnt):
    queue = deque([[num, jump, cnt]])
    while queue:
        now_num, jump, cnt = queue.popleft()
        if now_num == n:
            return cnt

        if jump - 1 != 0 and rock[now_num + jump - 1] and (now_num + jump -1, jump - 1) not in check:
            check.append((now_num + jump -1, jump - 1))
            queue.append([now_num + jump -1, jump - 1, cnt + 1])
        if now_num + jump + 1 <= n and rock[now_num + jump + 1]  and (now_num + jump + 1, jump + 1) not in check:
            check.append((now_num + jump + 1, jump + 1))
            queue.append([now_num + jump + 1, jump + 1, cnt + 1])
        if now_num + jump  <= n and rock[now_num + jump]  and (now_num + jump, jump) not in check:
            check.append((now_num + jump, jump))
            queue.append([now_num + jump, jump, cnt + 1])
        
        
n, m = map(int, sys.stdin.readline().split())

rock = [1 for _ in range(n + 1)]

for _ in range(m):
    idx = int(sys.stdin.readline())
    rock[idx] = 0

check = [(2, 1)]
print(bfs(2, 1, 1))

'''
