import sys
import heapq

N = int(sys.stdin.readline())
min_heap = []
max_heap = []
answer = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, num)

    if min_heap and min_heap[0] < max_heap[0][1]:
        min_heap_root = heapq.heappop(min_heap)
        max_heap_root = heapq.heapreplace(max_heap, (- min_heap_root, min_heap_root))
        heapq.heappush(min_heap, max_heap_root[1])

    print(max_heap[0][1])
    


