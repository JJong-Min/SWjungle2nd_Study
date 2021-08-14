import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([])
for _ in range(N):
    commands = sys.stdin.readline().split()
    if commands[0] == 'push':
        queue.append(commands[1])

    elif commands[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif commands[0] == 'size':
        print(len(queue))

    elif commands[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif commands[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)

    
        
