from collections import defaultdict, deque

def dikstra(i, N, road_list):
    values = [float('inf') for _ in range(N + 1)]
    values[i] = 0
    queue = deque([[1, 0]])
    while queue:
        x, v = queue.popleft()
        for new_x, new_v in road_list[x]:
            if new_v >= values[new_x]:
                continue
            if v + new_v < values[new_x]:
                values[new_x] = v + new_v
                queue.append([new_x, values[new_x]])
    return values
    
def solution(N, road, K):
    answer = 0
    road_list = [[]for _ in range(N + 1)]
    for x, y, v in road:
        road_list[x].append([y, v])
        road_list[y].append([x, v])
    values = dikstra(1, N, road_list)

    answer = len([i for i in values if i <= K])

    return answer

from queue import PriorityQueue

def dijkstra(road, N):
    queue = PriorityQueue()
    queue.put([1, 0])
    
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    
    while not queue.empty():
        current, current_cost = queue.get()
        for src, dest, cost in road:
            next_cost = current_cost + cost
            if current == src and next_cost < dist[dest]:
                dist[dest] = next_cost
                queue.put([dest, next_cost])
            elif current == dest and next_cost < dist[src]:
                dist[src] = next_cost
                queue.put([src, next_cost])
    return dist
    
def solution(N, road, K):
    dist  = dijkstra(road, N)
    return len([x for x in dist if x <= K])
