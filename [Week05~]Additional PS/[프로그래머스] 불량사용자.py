from collections import defaultdict
from itertools import product

def solution(user_id, banned_id):
    if len(user_id) == len(banned_id):
        return 1

    _dict = defaultdict(list)
    cnt= 1
    for _banned_id in banned_id:
        key_name = _banned_id
        if key_name in _dict:
            key_name = key_name + ('+' * cnt)
            cnt += 1
        for _user_id in user_id:
            if len(_banned_id) == len(_user_id):
                for i, j in zip(_banned_id, _user_id):
                    if i != '*' and i != j:
                        break
                else:
                    _dict[key_name].append(_user_id)
    
    if _dict == {}:
        return 0
    print(_dict)
    pd = product(*(_dict.values()))
    
    cand = set()
    answer = 0
    for i in pd:
        if len(_dict)  == len(set(i)):
            i = sorted(list(i))
            cand.add(tuple(i))

    return len(cand)
