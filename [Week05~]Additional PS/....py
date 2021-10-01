import sys
from queue import PriorityQueue
from collections import defaultdict

n, m, x = map(int, sys.stdin.readline().split())
roads = defaultdict(list)
for _ in range(m):
    s, d, c = map(int, sys.stdin.readline().split())
    roads[s].append([d, c])

queue = PriorityQueue()
queue.put([x, 0])
back = [float('inf') for _ in range(n + 1)]
back[x] = 0
while not queue.empty():
    node, cost = queue.get()
    for road in roads[node]:
        end, now_cost = road
        new_cost = cost + now_cost
        if new_cost < back[end]:
            back[end] = new_cost
            queue.put([end, new_cost])

for i in range(1, n + 1):
    if i == x:
        continue
    queue = PriorityQueue()
    queue.put([i, 0])
    go = [float('inf') for _ in range(n + 1)]
    go[i] = 0
    while not queue.empty():
        node, cost = queue.get()
        for road in roads[node]:
            end, now_cost = road
            new_cost = cost + now_cost
            if new_cost < go[end]:
                go[end] = new_cost
                queue.put([end, new_cost])
    back[i] += go[x]

print(max(back[1:]))
