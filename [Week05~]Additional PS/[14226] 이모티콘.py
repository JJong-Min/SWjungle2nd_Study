import sys
from collections import deque
#맞는 풀이
n = int(input())
dist = [[-1]* (n+1) for _ in range(n+1)]
q = deque()
q.append((1,0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수
dist[1][0] = 0
while q:
    s,c = q.popleft()
    if dist[s][s] == -1: # 방문하지 않았으면
        dist[s][s] = dist[s][c] + 1
        q.append((s,s))
    if s+c <= n and dist[s+c][c] == -1:
        dist[s+c][c] = dist[s][c] + 1
        q.append((s+c, c))
    if s-1 >= 0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))
answer = -1
for i in range(n+1):
    if dist[n][i] != -1:
        if answer == -1 or answer > dist[n][i]:
            answer = dist[n][i]
print(answer)

#내 풀이(틀림)
s = int(sys.stdin.readline())
copy_buf = 0
queue = deque([[1, 0]])


while queue:
    emoticon_num, cnt = queue.popleft()
    #삭제
    if emoticon_num - 1 >= 0:
        if emoticon_num - 1 == s:
            print(cnt + 1)
            break
        queue.append([emoticon_num - 1, cnt + 1])

    # 붙여넣기
    if copy_buf != 0:
        if emoticon_num + copy_buf == s:
            print(cnt + 1)
            break
        queue.append([emoticon_num + copy_buf, cnt + 1])

    #복사 후 붙여넣기
    copy_buf = emoticon_num
    if emoticon_num + copy_buf == s:
        print(cnt + 2)
        break
    queue.append([emoticon_num + copy_buf, cnt + 2])
