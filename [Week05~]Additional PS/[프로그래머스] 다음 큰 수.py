def solution(n):
    binary_n = format(n, 'b')
    n_one_count = list(str(binary_n)).count('1')
    next_n = n + 1
    binary_next_n = format(next_n, 'b')
    next_n_one_count = list(str(binary_next_n)).count('1')
    
    while n_one_count != next_n_one_count:
        next_n += 1
        binary_next_n = format(next_n, 'b')
        next_n_one_count = list(str(binary_next_n)).count('1')
    return next_n
