import math
def solution(names, homes, grades):
    answer = [0 for _ in range(len(names))]
    homes = [(x ** 2 + y ** 2) for x, y in homes]
    grades = [math.floor(x) for x in grades]
    total_list = []
    for i in range(len(names)):
        total_list.append((grades[i], homes[i], names[i], i))
    
    total_list = sorted(total_list, key=lambda x:(-x[0], -x[1], x[2]))
    
    for i in range(len(names)):
        answer[total_list[i][3]] = i + 1
    return answer
