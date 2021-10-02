import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)
        
        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]

    return [''.join(v) for v in sorted(result)]


from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        common = Counter()
        for j in orders:
            j = sorted(list(j))
            common += Counter(combinations(j, i))

        if common.most_common(1):
            most_common = common.most_common(1)[0][1]
            if most_common > 1:
                for _co in common:
                    if common[_co] == most_common:
                        answer.append(''.join(_co))
    answer = sorted(answer)
    return answer
