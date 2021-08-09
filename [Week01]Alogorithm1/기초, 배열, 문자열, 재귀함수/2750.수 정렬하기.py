import sys

# 선택 삽입 정렬
def insertion_sort(arr):
    length_arr = len(arr)

    for i in range(1, length_arr):
        init_idx = i
        tmp = arr[i]

        while init_idx > 0 and tmp < arr[init_idx - 1]:
            arr[init_idx] = arr[init_idx - 1]
            init_idx -= 1
        arr[init_idx] = tmp
            
    
arr = []
N = int(sys.stdin.readline())
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

insertion_sort(arr)
for i in arr:
    print(i)
