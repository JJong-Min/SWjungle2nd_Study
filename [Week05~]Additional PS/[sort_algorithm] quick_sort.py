def qsort(arr, left, right):
    pl = left
    pr = right
    pivot = arr[(left + right) // 2]

    while pl <= pr:
        while arr[pl] < pivot:
            pl += 1
        while arr[pr] > pivot:
            pr -= 1

        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1


    if left < pr:
        qsort(arr, left, pr)
    if pl < right:
        qsort(arr, pl, right)


def quick_sort(arr):
    qsort(arr, 0, len(arr) - 1)


def qsort_no_recur(arr, left, right):
    stack = []
    stack.append((left, right))

    while stack:
        pl, pr = left, right = stack.pop()
        pivot = arr[(left + right) // 2]

        while pl <= pr:
            while arr[pl] < pivot:
                pl += 1
            while arr[pr] > pivot:
                pr += 1

            if pl <= pr:
                arr[pl], arr[pr] = arr[pr], arr[pl]
                pl += 1
                pr -= 1

        if left < pr:
            stack.append((left, pr))
        if pl < right:
            stack.append((pl, right))
    
