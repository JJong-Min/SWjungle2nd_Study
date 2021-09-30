def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    while True:
        delete_set = set()
        for i in range(m):
            for j in range(n):
                try:
                    if board[i][j] == board[i][j + 1] == board[i + 1][j + 1] == board[i + 1][j] != "_":
                        delete_set.add((i, j))
                        delete_set.add((i, j + 1))
                        delete_set.add((i + 1, j))
                        delete_set.add((i + 1, j + 1))
                except IndexError:
                    continue
        if delete_set:
            for delete in delete_set:
                x, y = delete
                board[x][y] = "_"
                answer += 1
         
        else:
            break
        #행과 열 전환
        board = [list(i) for i in zip(*board)]
        #빈칸 앞으로 땡기기
        new_board = []
        for _board in board:
            _board = ["_"]  * _board.count("_") + [i for i in _board if i != "_"]
            new_board.append(_board)
        #다시 행과 열 전환
        board = [list(i) for i in zip(*new_board)]
    return answer

