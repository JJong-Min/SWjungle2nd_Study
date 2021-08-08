def selection_sort(n):
    length_arr = len(n)
    for i in range(length_arr - 1):
        min = i
        for j in range(i + 1, length_arr):
            if n[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
