from collections import defaultdict

def dfs(routes):
    stack = ["ICN"]
    path = []
    while stack:
        position = stack[-1]
        if position not in routes or len(routes[position]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[position].pop(0))
    return path[::-1]

def solution(tickets):
    routes = defaultdict(list)
    for departure, arrival in tickets:
        routes[departure].append(arrival)
        
    for route in routes:
        routes[route].sort()
    
    answer = dfs(routes)
        
    return answer
