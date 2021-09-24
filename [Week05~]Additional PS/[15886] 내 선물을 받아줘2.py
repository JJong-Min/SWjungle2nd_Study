import sys

n = int(sys.stdin.readline())
directions = list(sys.stdin.readline().rstrip())
check = [True for _ in range(n)]
candidate_ans = []

for i in range(n):
    check = [True for _ in range(n)]
    visited_position = set()
    x = i
    while check[x]:
        check[x] = False
        visited_position.add(x)
        if directions[x] == 'E':
            x += 1
        else:
            x -= 1
    candidate_ans.append(visited_position)

ans = candidate_ans[0]
cnt = 0
for i in range(1, n):
    if ans & candidate_ans[i] != set():
        ans = ans & candidate_ans[i]
    else:
        ans = candidate_ans[i]
        cnt += 1
    
print(cnt + 1)
