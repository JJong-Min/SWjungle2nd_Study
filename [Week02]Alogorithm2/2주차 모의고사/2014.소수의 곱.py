import sys
import heapq
k, n = map(int, sys.stdin.readline().split())
prime_nums = list(map(int, sys.stdin.readline().split()))
min_heap = []

for i in range(k):
    heapq.heappush(min_heap, prime_nums[i])

N = 0
while N != n:
    num = heapq.heappop(min_heap)
    N += 1
    for i in range(k):
        next_num = num * prime_nums[i]
        if next_num % 
