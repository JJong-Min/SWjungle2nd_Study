import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    card_num = int(sys.stdin.readline())
    heapq.heappush(heap, card_num)

answer = 0

while len(heap) > 1:
    card_A = heapq.heappop(heap)
    card_B = heapq.heappop(heap)
    answer += (card_A + card_B)
    heapq.heappush(heap, (card_A + card_B))

print(answer)
