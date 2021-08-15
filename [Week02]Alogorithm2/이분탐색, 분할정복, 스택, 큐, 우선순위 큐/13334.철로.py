import sys
import heapq

n = int(sys.stdin.readline())
people_locations = []
for _ in range(n):
    #h와 o를 [작은 수, 큰 수]로 받기 위해 조건문 처리
    h, o = map(int, sys.stdin.readline().split())
    if h <= o:
        people_locations.append([h, o])
    else:
        people_locations.append([o, h])

d = int(sys.stdin.readline())

# 집과 회사거리가 d보다 큰 것은 제거
people_locations = [(h, o) for h, o in people_locations if abs(h - o) <= d]
# 각자의 사람의 먼 위치를 기준으로 오름차순
people_locations.sort(key=lambda x: (x[1]))


heap = []
answer = 0

for people_location in people_locations:
    if not heap:
        heapq.heappush(heap, people_location[0])

    else:
        while heap[0] < people_location[1] - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, people_location[0])

    answer = max(answer, len(heap))

print(answer)
