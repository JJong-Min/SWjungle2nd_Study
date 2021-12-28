def insertion_sort(arr):
    arr_length = len(arr)
    for i in range(1, arr_length):
        tmp = arr[i]
        j = i
        while j > 0 and tmp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = tmp

'''
단순삽입정렬은 두 번째 원소부터 시작해 자신보다 앞에 있는 것을 대소비교를 하여 자신보다 크다면 계속 탐색을 하고
자신보다 작은 원소를 만나면 탐색을 멈추고 해당 자리에 삽입하는 방식이다.
'''

