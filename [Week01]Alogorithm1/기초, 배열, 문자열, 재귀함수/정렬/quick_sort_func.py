def qsort(arr, left, right):
    left_pointer = left
    right_pointer = right
    x = arr[(left + right) // 2]

    while left_pointer <= right_pointer:
        while arr[left_pointer] < x:
            left_pointer += 1
        while arr[right_pointer] > x:
            right_pointer -= 1

        if left_pointer <= right_pointer:
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]

            left_pointer += 1
            right_pointer -= 1

    if left < right_pointer:
        qsort(arr, left, right_pointer)
    if left_pointer < right:
        qsort(arr, left_pointer, right)

