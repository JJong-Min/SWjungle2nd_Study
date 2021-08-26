#큐사용(위상정렬)

'''
import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
branchs = [0 for _ in range(n + 1)]
toy_matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[y].append((x, k))
    branchs[x] += 1

queue = deque()

for i in range(1, n + 1):
    if branchs[i] == 0: 
        queue.append(i)


while queue:
    now_num = queue.popleft()
    for next_num1, next_num2 in graph[now_num]:
        # 현재노드(now_num)가 기본부품이면
        if toy_matrix[now_num].count(0) == n + 1:
            toy_matrix[next_num1][now_num] += next_num2

        else:
            for i in range(1, n + 1):
                toy_matrix[next_num1][i] += (next_num2 * toy_matrix[now_num][i])

        branchs[next_num1] -= 1
        if branchs[next_num1] == 0:
            queue.append(next_num1)
            
for i, v in enumerate(toy_matrix[n]):
    if v > 0:
        print(i, v)
'''

#DFS(위상정렬)
import sys
from collections import defaultdict

def dfs(i):
    if i == n:
        return 1
    if records[i] != 0:
        return records[i]

    v = 0
    for next_num in range(1, n + 1):
        if toy_matrix[next_num][i]:
            v += toy_matrix[next_num][i] * dfs(next_num)

    records[i] = v
    return v

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
toy_matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    toy_matrix[x][y] += k
    toy_matrix[0][x] += 1

result = defaultdict(int)
records = defaultdict(int)
for i in range(1, n + 1):
    if toy_matrix[0][i] == 0:
        result[i] = dfs(i)

for i in sorted(result):
    print(i, result[i])