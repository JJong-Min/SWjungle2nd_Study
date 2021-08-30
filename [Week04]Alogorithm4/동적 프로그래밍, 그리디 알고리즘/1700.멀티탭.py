import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
elec_products = list(map(int, sys.stdin.readline().split()))
now_multitap = set(elec_products[:n])
queue = deque(elec_products[n:])
cnt = 0

while queue:
    product = queue.popleft()
    if product in now_multitap or len(now_multitap) < n:
        now_multitap.add(product)
        continue

    delete_candidate = []
    for plugin_product in now_multitap:
        if plugin_product not in queue:
            now_multitap.remove(plugin_product)
            break
        delete_candidate.append(queue.index(plugin_product))
    else:
        now_multitap.remove(queue[max(delete_candidate)])
    now_multitap.add(product)
    cnt += 1

print(cnt)
            
