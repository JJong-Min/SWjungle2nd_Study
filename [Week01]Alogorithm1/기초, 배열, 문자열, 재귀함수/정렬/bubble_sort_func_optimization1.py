def bubble_sort(n):
    arr_length = len(n)
    for i in range(arr_length - 1):
    	exchange_num = 0
        for j in range(arr_length - 1, i, -1):
            if n[j - 1] > n[j]:
                n[j - 1], n[j] = n[j], n[j - 1]
                exchange_num += 1

        if exchange_num == 0:
            break
