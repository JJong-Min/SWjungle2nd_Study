# input 범위가 너무 크다, 개수도 만만치 않다.
# O(n^2)으로 풀면 시간초과가 날 것이다.
# 이분 검색을 실행하여 시간복잡도를 줄이자.

import sys

N, C = map(int ,sys.stdin.readline().split())
houses = []

for _ in range(N):
    houses.append(int(sys.stdin.readline()))

# 이분탐색을 위해 sort
houses.sort()

# 최소거리와 최대거리를 포인터로 설정
left_pointer = 1 # 최소거리는 좌표값이 연속된 숫자인 경우이므로 1
right_pointer = houses[-1] - houses[0] # 최대거리는 맨 끝 집과 맨 앞 집 사이 거리
answer = 0

# 이분 검색 시작
while left_pointer <= right_pointer:
    # 공유기 설치 인접 거리를 중앙값과 비교하며 검색
    middle = (left_pointer + right_pointer) // 2

    # 첫 번째 집에 공유기를 설치하고 시작
    C_ = 1
    before_house = houses[0]
    # 검색 시작
    for i in range(1, len(houses)):
        if houses[i] - before_house >= middle:
            C_ += 1
            before_house = houses[i]

    # 주어진 공유기 개수보다 적다면 범위를 줄여 middle값 줄이기
    if C_ < C:
        right_pointer = middle - 1

    # 그렇지 않고 더 많은 공유기를 설치했다면 범위를 늘려 middle값 늘리기
    else:
        left_pointer = middle + 1
        # middle 값을 저장해주는 이유는 조건에 충족해서 범위를 늘리거나 줄였을 때
        # 반복문이 break 될 수 있으므로 가장 최근의 가능했던 값을 저장
        answer = middle

print(answer)
