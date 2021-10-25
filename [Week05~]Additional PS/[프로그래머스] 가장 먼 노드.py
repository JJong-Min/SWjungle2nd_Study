from collections import defaultdict
import heapq

def dijkstra(start, n, graphs):
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[start] = 0
    heap = [[dist[start], start]]
    heapq.heapify(heap)
    
    while heap:
        cur_cost, cur_node = (heapq.heappop(heap))
        if dist[cur_node] < cur_cost:
            continue
        
        for new_node, new_cost in graphs[cur_node].items():
            add_cost = new_cost + cur_cost
            if add_cost < dist[new_node]:
                dist[new_node] = add_cost
                heapq.heappush(heap, [add_cost, new_node])
    return dist.values()
        
def solution(n, edge):
    graphs = defaultdict(dict)
    for node1, node2 in edge:
        graphs[node1][node2] = 1
        graphs[node2][node1] = 1
    answer = list(dijkstra(1, n, graphs))
    max_cost = max(answer)
    return answer.count(max_cost)


