import sys

sys.setrecursionlimit(10**8)
def dfs(n):
   for i in trees[n]:
       if not answer[i]:
           answer[i].append(n)
           dfs(i)


n = int(sys.stdin.readline())
trees = [[] for _ in range(n + 1)]
answer = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, sys.stdin.readline().split())
    trees[x].append(y)
    trees[y].append(x)

dfs(1)

for idx in range(2, n + 1):
    print(answer[idx][0])
