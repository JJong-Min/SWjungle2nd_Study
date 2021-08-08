def insertion_sort(arr):
    length_arr = len(arr)
    for i in range(1, length_arr):
        j = i
        tmp = arr[i]
        while j > 0 and arr[j - 1] > tmp:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = tmp
