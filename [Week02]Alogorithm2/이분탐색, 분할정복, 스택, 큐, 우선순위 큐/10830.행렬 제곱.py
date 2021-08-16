import sys
            
def new_matrix(matrix1, matrix2, n):
    result = [[] for _ in range(n)]
    matrix_2 = [i for i in zip(*matrix2)]
    for i in range(n):
        for j in range(n):
            multi_num = sum([num1 * num2 for num1, num2 in zip(matrix1[i], matrix_2[j])])
            result[i].append(multi_num % 1000)

    return result

def squared_matrix(matrix, n, b):
    if b == 1:
        return matrix
    
    if b == 2:
        return new_matrix(matrix, matrix, n)


    temp = squared_matrix(matrix, n, b // 2)

    if b % 2 == 0:
        return new_matrix(temp, temp, n)

    else:
        return new_matrix(new_matrix(temp, temp, n), matrix, n)
    
N, B = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    print(*squared_matrix(matrix, N, B)[i])
    
