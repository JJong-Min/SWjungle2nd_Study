def solution(n, horizontal):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    if horizontal:
        move = [(0, 1), (1, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]

    else:
        move = [(1, 0), (0, 1), (-1, 0), (0, 1), (1, 0), (0, -1)]

    end_num = n * n
    d = 0
    now_x = 0
    now_y = 0
    now_num = 1
    end_line = 2

    while (now_num <= end_num):

        answer[now_x][now_y] = now_num
        
        if now_x + move[d][0] < 0 or now_x + move[d][0] >= end_line or now_y + move[d][1] < 0 or now_y + move[d][1] >= end_line:
            d = (d + 1) % 6
        if (end_line ** 2) == now_num:
            end_line += 1

        now_x = now_x + move[d][0]
        now_y = now_y + move[d][1]
        now_num += 1

    return answer

n = 5
horizontal = False

print(solution(n, horizontal))
           
        
