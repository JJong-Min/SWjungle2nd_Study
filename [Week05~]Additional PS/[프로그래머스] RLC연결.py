
from collections import defaultdict

def solution(rows, columns, connections, queries):
    answer = []
    conn_dict = defaultdict(list)
    deconnections = set()
    
    for r1, c1, r2, c2 in connections:
        conn_dict[(r1, c1)].append((r2, c2))
        conn_dict[(r2, c2)].append((r1, c1))

    print(conn_dict)
    for query in queries:
        set_query = set()
        r1, c1, r2, c2 = query
        min_r = min(r1, r2)
        max_r = max(r1, r2)
        min_c = min(c1, c2)
        max_c = max(c1, c2)
    
        for c in range(min_c, max_c + 1):
            set_query.add((min_r, c))
            set_query.add((max_r, c))
        
        for r in range(min_r, max_r + 1):
            set_query.add((r, min_c))
            set_query.add((r, max_c))

        print(set_query)
        cnt = 0
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for _r1, _c1 in set_query:
            print(deconnections)
            if (_r1, _c1) not in conn_dict.keys():
                continue
                
            for j in range(4):
                _r2, _c2 = _r1 + delta[j][0], _c1 + delta[j][1]
                print('_r1, c1:', (_r1, c1), '_r2, c2:',(_r2, _c2))
                print((_r2, _c2) not in set_query)
                print((_r2, _c2) in conn_dict[(_r1, _c1)])
                print((_r2, _c2) not in deconnections)
                if 0 <= _r2 <= rows and 0 <= _c2 <= columns:
                    if (_r2, _c2) not in set_query and (_r2, _c2) in conn_dict[(_r1, _c1)] and (_r1, _c1, _r2, _c2) not in deconnections:
                        cnt += 1
                        deconnections.add((_r1, _c1, _r2, _c2))
                        deconnections.add((_r1, _c1, _r2, _c2))
        
        answer.append(cnt)
    return answer

rows = 2
columns = 2
connections = [[1,1,1,2],[2,2,1,2],[2,1,1,1],[2,2,2,1]]
queries = [[1,1,2,2],[1,1,2,1],[2,1,2,2]]

print(solution(rows, columns, connections, queries))
