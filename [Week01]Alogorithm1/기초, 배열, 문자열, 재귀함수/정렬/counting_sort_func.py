def fsort(arr, max_num):
    n = len(arr)
    f = [0] * (max_num + 1)
    b = [0] * n

    for i in range(n):
        f[arr[i]] += 1

    for i in range(1, max_num + 1):
        f[i] += f[i - 1]

    for i in range(n - 1, -1, -1):
        f[arr[i]] -= 1
        b[f[arr[i]]] = arr[i]
        
    for i in range(n):
        arr[i] = b[i]

def counting_sort(a):
    fsort(a, max(a))


