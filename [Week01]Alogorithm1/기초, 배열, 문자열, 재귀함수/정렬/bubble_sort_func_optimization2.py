def bubble_sort(n):
    arr_length = len(n)
    k = 0
    while k < n - 1:
    	exchange_num = 0
        for j in range(arr_length - 1, i, -1):
            if n[j - 1] > n[j]:
                n[j - 1], n[j] = n[j], n[j - 1]
                exchange_num += 1
                k = j
   
        if exchange_num == 0:
            break
