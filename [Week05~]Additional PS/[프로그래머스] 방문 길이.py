def solution(dirs):
    answer = 0
    dict = {'U':(1, 0), 'D':(-1, 0), 'R':(0, 1), 'L':(0, -1)}
    now_point = (0, 0)
    visited_route = set()

    for dir in dirs:
        now_x = now_point[0]
        now_y = now_point[1]
        move_x, move_y = dict[dir]
        next_x, next_y = now_x + move_x, now_y + move_y
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            now_point = (next_x, next_y)
            visited_route.add(((now_x, next_x), (now_y, next_y)))
            visited_route.add(((next_x, now_x), (next_y, now_y)))
        
        answer = len(visited_route) // 2
    return answer 
