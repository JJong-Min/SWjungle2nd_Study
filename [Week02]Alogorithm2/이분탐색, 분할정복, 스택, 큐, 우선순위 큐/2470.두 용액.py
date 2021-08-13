import sys

N = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))
solutions.sort()

min_value = solutions[0] + solutions[-1]
# 답을 저장하는 변수
ans_left_idx = 0
ans_right_idx = N - 1
# 투 포인터로 반복문을 돌기 위한 변수
left_pointer = 0
right_pointer = N - 1


while left_pointer < right_pointer:
    new_value = solutions[left_pointer] + solutions[right_pointer]

    # 이전까지 탐색에서 얻은 min_value와 현재 용액의 합과 비교
    if abs(min_value) > abs(new_value):
        min_value = new_value
        ans_left_idx = left_pointer
        ans_right_idx = right_pointer

        # 만약, 구한 용액의 합이 0이면 바로 반복문 종료 후 답 제출
        # 답이 2개 이상인 경우 아무거나 제출가능하므로
        if new_value == 0:
            break
    # 용액의 합이 음수이면 왼쪽 포인터를 이동해서 합이 0에 가깝게 해줌
    if new_value < 0:
        left_pointer += 1
    # 양수면 오른쪽 포인터를 이동해서 합이 0에 가깝게 해줌
    else:
        right_pointer -= 1

print(solutions[ans_left_idx], solutions[ans_right_idx])
            

    
