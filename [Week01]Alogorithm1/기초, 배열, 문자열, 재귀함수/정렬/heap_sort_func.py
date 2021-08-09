def heap_sort(arr):

    def down_heap(arr, left, right):
        temp = arr[left]
        parent = left
        while parent < (right + 1) // 2:
            child_left = parent * 2 + 1
            child_right = child_left + 1
            child = child_right if child_right <= right and arr[child_right] > arr[child_left] else child_left
            if temp >= arr[child]:
                break
            arr[parent] = arr[child]
            parent = child
        arr[parent] = temp

    n = len(arr)

    for i in range((n - 1) // 2, -1, -1):
        down_heap(arr, i, n - 1)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        down_heap(arr, 0, i - 1)

