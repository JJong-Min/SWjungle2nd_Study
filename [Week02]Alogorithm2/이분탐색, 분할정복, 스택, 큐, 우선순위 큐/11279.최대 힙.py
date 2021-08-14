import sys
import heapq

arr = []
heapq.heapify(arr)

N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)

    else:
        heapq.heappush(arr, (-x, x))
