import sys

# 후보군 중 0을 포함하거나 숫자가 2개 들어간 수들은 제외
candidate_nums = [0 for _ in range(123)] + [1 for _ in range(123, 1000)]

# for문은 돌면서 0을 포함하거나 숫자가 2개 들어간 수들은 제외
for i in range(123, 1000):
    if str(i)[0] == str(i)[1] or str(i)[1] == str(i)[2] or str(i)[0] == str(i)[2]:
        candidate_nums[i] = 0

    elif '0' in str(i):
        candidate_nums[i] = 0


# input 받기
N = int(sys.stdin.readline())
for _ in range(N):
    question, strike_num, ball_num = sys.stdin.readline().split()
    for candidate_num in range(123, 1000):
        # 후보군 배열 중 가능한 것만 비교
        if candidate_nums[candidate_num] == 1:
            candidate_num = str(candidate_num)
            strike_num_ = 0
            ball_num_ = 0
            for idx_1 in range(3):
                for idx_2 in range(3):
                    # 숫자가 같은데 위치도 같으면 strike 처리
                    if idx_1 == idx_2 and question[idx_1] == candidate_num[idx_2]:
                        strike_num_ += 1
                    # 숫자가 같은데 다른 위치이면 ball 처리
                    elif idx_1 != idx_2 and question[idx_1] == candidate_num[idx_2]:
                        ball_num_ += 1

            # 정답으로 주어진 스트라이크 볼 개수와 직접 비교하여 알아낸
            # 스트라이크와 볼 개수가 다르면 후보군에서 제외
            if int(strike_num) != strike_num_ or int(ball_num) != ball_num_:
                  candidate_nums[int(candidate_num)] = 0

print(candidate_nums.count(1))

            
            
            
