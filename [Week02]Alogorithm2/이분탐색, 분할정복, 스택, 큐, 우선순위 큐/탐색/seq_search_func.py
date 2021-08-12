# while문 사용
def seq_search(arr, key):
    i= 0

    while True:
        if i == len(arr):
            return -1
        if arr[i] == key:
            return i
        i += 1

# for문 사용
def seq_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i

    return -1
