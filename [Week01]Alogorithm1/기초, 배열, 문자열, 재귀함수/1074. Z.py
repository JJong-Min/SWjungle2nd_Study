# 반복문으로 구현(시간 초과)
import sys
N, r, c = map(int, sys.stdin.readline().split())
count = 0
while N > 1:
    benchmark = 2 ** (N - 1)
    if r >= benchmark:
        if c >= benchmark:
            count += 4 ** (N - 1) * 3
            r -= benchmark
            c -= benchmark

        else:
            count += 4 ** (N - 1) * 2
            r-= benchmark
    else:
        if c >= benchmark:
            count += 4 ** (N - 1)
            c -= benchmark
        else:
            continue
    N -= 1


if r == 0:
    if c == 0:
        print(count)
    else:
        print(count + 1)
else:
    if c == 0:
        print(count + 2)
    else:
        print(count + 3)

# 재귀함수로 구현(통과)
import sys


def z_solution(n, r, c, count):
    if n == 1:
        if r == 0:
            # 2사분면인 경우
            if c == 0:
                print(count)
            # 1사분면인 경우
            else:
                print(count + 1)
        else:
            # 3사분면인 경우
            if c == 0:
                print(count + 2)
            # 4사분면인 경우
            else:
                print(count + 3)
        return

    else:
        # 현재 배열의 절반 위치
        middle_point = 2 ** (n - 1)
        if r >= middle_point:
            #4사분면인 경우
            if c >= middle_point:
                count += 4 ** (n - 1) * 3
                r -= middle_point
                c -= middle_point
            # 3사분면인 경우
            else:
                count += 4 ** (n - 1) * 2
                r -= middle_point

        else:
            # 1사분면인 경우
            if c >= middle_point:
                count += 4 ** (n - 1)
                c -= middle_point

        z_solution(n - 1, r, c, count)

N, r, c = map(int, sys.stdin.readline().split())
z_solution(N, r, c, 0)
