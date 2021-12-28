def selection_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len - 1):
        min_idx = i
        for j in range(i + 1, arr_len):
            if arr[i] < arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

'''
선택 정렬은 오름차순 시에는 정렬하고자하는 범위 내에서 가장 작은 원소를 선택하여
해당 범위 내의 맨 앞 원소와 위치를 바꿔가면서 정렬하는 것이다.
(내림차순 시에는 가장 큰 원소를 앞으로)
이 또한 n -1번 연산을 반복해야한다.
'''
    
