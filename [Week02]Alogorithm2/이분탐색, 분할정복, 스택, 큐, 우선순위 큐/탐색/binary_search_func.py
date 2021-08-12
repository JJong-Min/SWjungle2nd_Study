import sys

def binary_search(arr, key):
    left_pointer = 0
    right_pointer = len(arr) - 1

    while left_pointer <= right_pointer:
        middle_point = (left_pointer + right_pointer) // 2
        if key == arr[middle_point]:
            return middle_point

        elif key < arr[middle_point]:
            right_pointer = middle_point - 1
        else:
            left_pointer = middle_point + 1

    return -1
