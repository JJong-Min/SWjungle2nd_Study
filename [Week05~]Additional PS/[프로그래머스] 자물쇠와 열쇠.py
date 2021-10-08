def expand_lock(lock, N, M, size):
    expanded_lock = [[0 for i in range(size)] for _ in range(size)]
    for x in range(N):
        for y in range(N):
            expanded_lock[x + M - 1][y + M - 1] = lock[x][y]

    return expanded_lock

def rotate(key):
    # *key는 껍질(Unpacking)을 벗겨내는 역할을 합니다. [] () {}
    # [[0, 0, 0], [1, 0, 0], [0, 1, 1]] key
    # [0, 0, 0], [1, 0, 0], [0, 1, 1] *key
    # (0, 1, 0), (0, 0, 1), (0, 0, 1) zip(*key)
    # (0, 1, 0), (1, 0, 0), (1, 0, 0) reversed
    # [0, 1, 0], [1, 0, 0], [1, 0, 0] list
    # [[0, 1, 0], [1, 0, 0], [1, 0, 0]] []
    
    return [list(reversed(i)) for i in zip(*key)]

def is_unlock(x, y, key, lock, N, M):
    _lock = [item[:] for item in lock]
    for _x in range(M):
        for _y in range(M):
            _lock[_x + x][_y + y] += key[_x][_y]

    for _x in range(N):
        for _y in range(N):
            if _lock[_x + M - 1][_y + M - 1] != 1:
                return False

    return True

def solution(key, lock):
    N = len(lock)
    M = len(key)
    size = (M - 1) * 2 + N
    expanded_lock = expand_lock(lock, N, M, size)

    for _ in range(4):
        for x in range(size - M + 1):
            for y in range(size - M + 1):
                if is_unlock(x, y, key, expanded_lock, N, M):
                    return True
        key = rotate(key)

    return False
