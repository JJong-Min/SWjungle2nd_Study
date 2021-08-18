import sys
'''
def binary_search(arr, key):
    left_pointer = 0
    right_pointer = len(arr) - 1

    while left_pointer <= right_pointer:
        middle_point = (left_pointer + right_pointer) // 2
        if key == arr[middle_point]:
            return 1

        elif key < arr[middle_point]:
            right_pointer = middle_point - 1
        else:
            left_pointer = middle_point + 1

    return 0

N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))
arr1.sort()

for i in arr2:
    print(binary_search(arr1, i))

'''
# 시간 복잡도 줄이기 (O(N + M))
from collections import defaultdict
N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

arr1_dict = defaultdict(int)
for i in arr1:
    arr1_dict[i] = 1
    
for j in arr2:
    if arr1_dict[j] == 0:
        print(0)
    else:
        print(1)

