import sys
from collections import deque

n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
queue = deque()

for d, p in zip(distance, price):
    queue.append([d, p])

final_price = 0
standard_price = float('inf')

while queue:
    now_distance, now_price = queue.popleft()
    standard_price = min(standard_price, now_price)
    final_price += now_distance * standard_price

print(final_price)
