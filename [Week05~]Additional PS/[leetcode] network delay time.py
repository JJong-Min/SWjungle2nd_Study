class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graphs = collections.defaultdict(dict)
        for start, dest, cost in times:
            graphs[start - 1][dest - 1] = cost
        
        answer = [float('inf') for _ in range(n)]
        def dijkstra(k):
            heap = [[0, k]]
            heapq.heapify(heap)
            answer[k] = 0
            while heap:
                cur_cost, cur_node = heapq.heappop(heap)
                
                for node, cost in graphs[cur_node].items():
                    add_cost = cur_cost + cost
                    if add_cost < answer[node]:
                        answer[node] = add_cost
                        heapq.heappush(heap, [add_cost, node])
        dijkstra(k - 1)
        
        if float('inf') in answer:
            return -1
        else:
            return max(answer)

