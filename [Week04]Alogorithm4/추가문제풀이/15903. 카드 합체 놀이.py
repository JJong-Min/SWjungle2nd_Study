import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
heapq.heapify(nums)

for _ in range(m):
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    heapq.heappush(nums, a + b)
    heapq.heappush(nums, a + b)

print(sum(nums))
