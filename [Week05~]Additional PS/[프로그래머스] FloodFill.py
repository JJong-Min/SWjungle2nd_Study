from collections import deque

def solution(n, m, image):
    answer = 0
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    for sy in range(n):
        for sx in range(m):
            if image[sy][sx] == float('inf'):
                continue

            target_color = image[sy][sx]
            queue = deque([(sy, sx)])

            while queue:
                y, x = queue.popleft()

                for dy, dx in directions:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= nx < m and 0 <= ny < n and image[ny][nx] == target_color:
                        image[ny][nx] = float('inf')
                        queue.append((ny, nx))

            answer += 1
    
    return answer
