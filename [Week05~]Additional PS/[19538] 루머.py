import sys
from collections import deque
'''

def solution(N, E, M, firstInfected):
    Q = deque([]) # 감염된 사람의 번호를 큐에 저장할 것이다.
    answer = [-1] * (N+1) # solution 함수에서 리턴할 배열, 사이즈 N+1, -1로 초기화
    turn = [0] * (N+1) # 감염까지 남은 주변 비감염 사람 수, 사이즈 N+1, 0로 초기화

    for t in firstInfected:
        Q.append(t)
        answer[t] = 0

  
    for i in range(1, N+1):
        turn[i] = (len(E[i])) // 2

    while Q:
        current = Q.popleft()
        for next in E[current]:
            if next == 0:
                break
            turn[next] -= 1
            if answer[next] == -1 and turn[next] <= 0:
                Q.append(next)
                answer[next] = answer[current] + 1

    return answer[1:] 


input = sys.stdin.readline
N = int(input())
E = [[] for _ in range(N+1)]
for i in range(1, N+1):
    E[i] = list(map(int, input().split()))

M = int(input())
firstInfected = list(map(int, input().split()))
print(" ".join(map(str, solution(N, E, M, firstInfected))))

'''
import sys, math
from collections import deque

def bfs(rumor, t):
    queue = deque([[rumor, t]])
    while queue:
        people, _t = queue.popleft()
        answer[people - 1] = _t
        for i in relations[people]:
            half[i] -= 1
            if answer[i - 1] == -1 and half[i] <= 0:
                queue.append([i, _t + 1])

n = int(sys.stdin.readline())
relations = {}
half = {}
for i in range(n):
    people = map(int, sys.stdin.readline().split())
    people = [j for j in people if j != 0]
    relations[i + 1] = people
    half[i + 1] = math.ceil(len(people) / 2)
    
m = int(sys.stdin.readline())
rumors = list(map(int, sys.stdin.readline().split()))

answer = [-1 for _ in range(n)]
t = 0

for rumor in rumors:
    bfs(rumor, t)

print(*answer)
