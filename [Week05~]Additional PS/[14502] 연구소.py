import sys
from itertools import combinations
import copy

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(x, y):
    for i in range(4):
        nx = x + delta[i][0]
        ny = y + delta[i][1]
        if 0 <= nx < n and 0 <= ny < m and _graph[nx][ny] == 0:
            _graph[nx][ny] = 2
            dfs(nx, ny)

def count(graph):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1

    return cnt

n, m = map(int, sys.stdin.readline().split())
empty =[]
virus = []
graph = []
answer = 0

for i in range(n):
    _list = list(map(int, sys.stdin.readline().split()))
    graph.append(_list)
    for j in range(m):
        if _list[j] == 0:
            empty.append((i, j))
        elif _list[j] == 2:
            virus.append((i, j))
    
available_empties = list(combinations(empty, 3))

for available_empty in available_empties:
    point1, point2, point3 = available_empty
    _graph = copy.deepcopy(graph)
    _graph[point1[0]][point1[1]] = _graph[point2[0]][point2[1]] = _graph[point3[0]][point3[1]] = 1

    for vir in virus:
        x, y = vir
        dfs(x, y)

    answer = max(answer, count(_graph))

print(answer)
    

    
