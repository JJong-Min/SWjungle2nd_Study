# 내 풀이 (틀린 풀이)
import sys
import heapq

white_heap = []
black_heap = []
heapq.heapify(white_heap)
heapq.heapify(black_heap)

for i in range(31):
    white, black = map(int, sys.stdin.readline().split())
    heapq.heappush(white_heap, (-white, i))
    heapq.heappush(black_heap, (-black, i))

check = [False for _ in range(31)]
ans = 0

for _ in range(15):
    point, num = heapq.heappop(white_heap)
    while check[num]:
        point, num = heapq.heappop(white_heap)
    ans -= point
    check[num] = True

    point, num = heapq.heappop(black_heap)
    while check[num]:
        point, num = heapq.heappop(black_heap)
    ans -= point
    check[num] = True

print(ans)


# 맞은 풀이 (top-down, 반복문)
li = []
while True:
    try:
        temp = list(map(int, input().split()))
        li.append(temp)
    except:
        break

dp = [[0] * 16 for _ in range(16)] # dp[w][b]
for white, black in li:
    for w in range(15, -1, -1):
        for b in range(15, -1, -1):
            if w - 1 < 0 and b - 1 < 0:
                continue
            elif w - 1 < 0:
                dp[w][b] = max(dp[w][b - 1] + black, dp[w][b])
            elif b - 1 < 0 :
                dp[w][b] = max(dp[w - 1][b] + white, dp[w][b])
            else:
                dp[w][b] = max(dp[w - 1][b] + white, dp[w][b - 1] + black, dp[w][b])
            
print(dp[15][15])

# 맞은 풀이 (top-down, 재귀)
def dfs(white, black, current_index, length):

    if white == 0 and black == 0:
        return 0
    if current_index == length:
        return 0
    if dp[current_index][white][black] != 0:
        return dp[current_index][white][black]

    dp[current_index][white][black] = dfs(white, black, current_index+1, length)
    if white > 0:
        dp[current_index][white][black] = max(dp[current_index][white][black], dfs(white-1, black, current_index+1, length) + wl[current_index])
    if black > 0:
        dp[current_index][white][black] = max(dp[current_index][white][black], dfs(white, black-1, current_index+1, length) + bl[current_index])
    return dp[current_index][white][black]

wl, bl = [], []
length = 0
total = 0

while True:
    try:
        w, b = map(int, input().split())
        length += 1
    except:
        break
    wl.append(w)
    bl.append(b)

dp = [[[0] * 16 for _ in range(16)] for _ in range(length+1)]
print(dfs(15, 15, 0, length))
