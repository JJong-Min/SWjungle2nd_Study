# 9점
'''
import sys

M, N, L = map(int, sys.stdin.readline().split())
shooters = list(map(int, sys.stdin.readline().split()))
shooters.sort()

animals = []
answer = 0
for _ in range(N):
    animals.append(list(map(int, sys.stdin.readline().split())))

for animal in animals:
    left = 0
    right = M - 1
    while left <= right:
        mid = (left + right) // 2
        if abs(shooters[mid] - animal[0]) + animal[1] <= L:
            answer += 1
            break
        else:
            if animal[0] > L:
                left = mid + 1
            else:
                right = mid - 1

print(answer)
'''
# 100
import sys

M, N, L = map(int, sys.stdin.readline().split())
shooters = list(map(int, sys.stdin.readline().split()))
shooters.sort()

animals = []
answer = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if y <= L:
        animals.append([x, y])

animals.sort(key= lambda x: x[0])

for animal in animals:
    left = 0
    right = M - 1
    while left <= right:
        mid = (left + right) // 2
        if abs(shooters[mid] - animal[0]) + animal[1] <= L:
            answer += 1
            break
        else:
            if animal[0] > shooters[mid]:
                left = mid + 1
            else:
                right = mid - 1

print(answer)
    
    
