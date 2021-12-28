def bubble_sort(arr):
    arr_length = len(arr)
    for i in range(arr_length - 1):
        for j in range(arr_length - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

'''
버블소트는 이웃하는 두 원소의 대소관계를 비교하여 위치를 바꾸는 연산을 사용하여
정렬를 하는 알고리즘이다.
만약에 오름차순으로 정렬한다고 한다면 맨 뒷 원소부터 이웃하는 원소와 비교하면서
왼쪽 원소가 오른쪽 원소보다 크다면 위치를 swap하는 방식을 택한다.
이렇게 하면 맨 처음 원소에는 가장 작은 수가 위치할 수 있고 이 연산을 n - 1번
반복하면 오름차순 정렬이 완성된다.
'''

