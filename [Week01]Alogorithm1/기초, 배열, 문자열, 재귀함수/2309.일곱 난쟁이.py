import sys
from collections import deque

little_persons = []
for _ in range(9):
    little_persons_height = int(sys.stdin.readline())
    little_persons.append(little_persons_height)

little_persons_height_sum = sum(little_persons)
remove_height = little_persons_height_sum - 100

queue = deque(little_persons)

while True:
    height = queue.popleft()
    remain_height = remove_height - height
    if remain_height in queue:
        queue.remove(remain_height)
        break
    else:
        queue.append(height)



little_persons = list(queue)
little_persons.sort()
for i in little_persons:
    print(i)
