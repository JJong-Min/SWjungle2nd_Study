import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    
    score_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    score_list.sort()
    standard_rank = score_list[0][1]
    cnt = 1
    for idx in range(1, n):
        if standard_rank >= score_list[idx][1]:
            cnt += 1
            standard_rank = score_list[idx][1]

    print(cnt)


# 16퍼 틀렸습니다.
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    
    score_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    score_list.sort()
    cnt = 0
    score1, score2 = score_list[0]
    tmp = 0
    for idx in range(1, n):
        if score1 >= score_list[idx][0] or score2 >= score_list[idx][1]:
            tmp += 1
        else:
            tmp += 1
            cnt = max(tmp, cnt)
            tmp = 0
            score1, score2 = score_list[idx]

    cnt = max(cnt, tmp + 1)

    print(cnt)
    
        
        
    


