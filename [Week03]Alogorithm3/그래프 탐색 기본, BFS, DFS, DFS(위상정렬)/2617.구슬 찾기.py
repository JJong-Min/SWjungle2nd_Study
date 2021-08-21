import sys

def dfs(x, beads):
    global cnt
    check[x] = False
    for i in beads[x]:
        if check[i]:
            cnt += 1
            dfs(i, beads)
            
    return cnt

n, m = map(int, sys.stdin.readline().split())
heavy_beads = [[] for _ in range(n + 1)]
light_beads = [[] for _ in range(n + 1)]
standard = n // 2

for _ in range(m):
   x, y = map(int, sys.stdin.readline().split())
   heavy_beads[x].append(y)
   light_beads[y].append(x)

ans = 0
for i in range(1, n + 1):
    cnt = 0
    check = [True for _ in range(n + 1)]
    if dfs(i, heavy_beads) > standard:
        ans += 1

    cnt = 0
    check = [True for _ in range(n + 1)]
    if dfs(i, light_beads) > standard:
        ans += 1

print(ans)
