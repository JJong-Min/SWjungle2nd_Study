from collections import deque
import copy
def solution(record):
    answer = []
    perchase_cost = deque([])
    sell_count = 0
    first_sell_cost = 0
    last_sell_cost = 0
    
    for _record in record:
        _record = _record.split()
        if _record[0] == 'P':
            for count in range(int(_record[-1])):
                perchase_cost.append(int(_record[1]))
        
        else:
            sell_count += int(_record[-1])

    while sell_count != 0:
        first_sell_cost += perchase_cost.popleft()
        sell_count -= 1
        
    answer.append(first_sell_cost)

    perchase_cost = deque([])
    for _record in record:
        _record = _record.split()
        if _record[0] == 'P':
            for count in range(int(_record[-1])):
                perchase_cost.append(int(_record[1]))

        else:
            count = int(_record[-1])
            while count != 0:
                last_sell_cost += perchase_cost.pop()
                count -= 1
    
    answer.append(last_sell_cost)            

    return answer

record = ["P 300 6", "P 500 3", "S 1000 4", "P 600 2", "S 1200 1"]
print(solution(record))
