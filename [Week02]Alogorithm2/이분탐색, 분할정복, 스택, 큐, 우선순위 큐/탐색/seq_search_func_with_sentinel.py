# 보초를 추가한 선형정렬
import copy
def seq_search(seq, key):
    arr = copy.deepcopy(seq)
    arr.append(key)

    i = 0
    while arr[i] != key:
        i += 1

    return -1 if i == len(seq) else i

