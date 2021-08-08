def binary_insertion_sort(arr):
    length_arr = len(arr)
    for i in range(1, length_arr):
        key = arr[i]
        first_searching_index = 0
        last_searching_index = length_arr - 1

        while True:
            center_searching_index = (first_searching_index + last_searching_index) // 2
            if arr[center_searching_index] == key:
                break

            elif arr[center_searching_index] < key:
                first_searching_index = center_searching_index + 1

            else:
                last_searching_index = center_searching_index - 1

            if first_searching_index > last_searching_index:
                break

    insertion_index = center_searching_index - 1 if first_searching_index <= last_searching_index else last_searching_index + 1

    for j in range(i, insertion_index, -1):
        arr[j] = arr[j - 1]
    arr[insertion_index] = key
