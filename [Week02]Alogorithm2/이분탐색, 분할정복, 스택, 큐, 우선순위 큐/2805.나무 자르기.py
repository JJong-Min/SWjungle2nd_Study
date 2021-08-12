import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

left_pointer = 0
right_pointer = max(trees)

while left_pointer <= right_pointer:
    middle = (left_pointer + right_pointer) // 2
    total_cut_trees = sum([i - middle for i in trees if i - middle > 0])
    if total_cut_trees >= M:
        left_pointer = middle + 1

    else:
        right_pointer = middle - 1

print(right_pointer)
