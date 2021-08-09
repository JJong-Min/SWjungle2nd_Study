import sys

def merge_sort(arr):

    def _merge_sort(arr, left, right):
        if left < right:
            center = (left + right) // 2

            _merge_sort(arr, left, center)
            _merge_sort(arr, center + 1, right)

            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = arr[i]
                p += 1
                i += 1

            while i <= right and j < p:
                if buff[j] <= arr[i]:
                    arr[k] = buff[j]
                    j += 1

                else:
                    arr[k] = arr[i]
                    i += 1
                k += 1


            while j < p:
                arr[k] = buff[j]
                k += 1
                j += 1

    n = len(arr)
    buff = [None] * n
    _merge_sort(arr, 0, n - 1)

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

merge_sort(arr)
for i in arr:
    print(i)
