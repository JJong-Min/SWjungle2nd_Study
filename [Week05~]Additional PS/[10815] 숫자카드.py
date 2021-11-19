import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
answer = [0 for _ in range(m)]

for k, number in enumerate(m_list):
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if n_list[middle] == number:
            answer[k] = 1
            break

        elif n_list[middle] < number:
            left = middle + 1

        else:
            right = middle - 1

print(*answer)
