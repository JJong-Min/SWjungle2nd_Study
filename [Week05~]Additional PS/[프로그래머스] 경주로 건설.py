from collections import deque

def solution(board):
    answer = -1
    board_size = len(board)
    queue = deque([(0, 0, -1, 0)]) # x, y, direction, cost
    visit_cost = [[-1 for _ in range(board_size)] for _ in range(board_size)]
    
    while queue:
        x, y, direction, cost = queue.popleft()
        if x == board_size - 1 and y == board_size - 1 and (answer == -1 or answer > cost):
            answer = cost
        
        to_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i, to_direction in enumerate(to_directions):
            dx, dy = to_direction
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < board_size and 0 <= ny < board_size and board[nx][ny] == 0:
                now_cost = cost + (100 if direction == i or direction == -1 else 600)
                if visit_cost[nx][ny] != -1 and visit_cost[nx][ny] < now_cost:
                    continue
            
                queue.append((nx, ny, i, now_cost))
                visit_cost[nx][ny] = now_cost
        
    
    return answer
