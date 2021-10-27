from collections import defaultdict

def dfs(node, check, networks):
    check[node] = True
    for next_node in networks[node]:
        if not check[next_node]:
            dfs(next_node, check, networks)
            
def solution(n, computers):
    networks = defaultdict(list)
    for node1, computer in enumerate(computers):
        for node2, connection in enumerate(computer):
            if connection == 1:
                networks[node1].append(node2)

    check = [False for _ in range(n)]
    answer = 0
    for i in range(n):
        if not check[i]:
            answer += 1
            dfs(i, check, networks)
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
