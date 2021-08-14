import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([i for i in range(1, N + 1)])

while len(queue) > 1:
    queue.popleft()
    top_num = queue.popleft()
    queue.append(top_num)

print(queue[0])
    
        
