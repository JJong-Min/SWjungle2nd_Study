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
