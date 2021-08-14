import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
LIS = [1] * N
for i in range(1, N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            LIS[i] = max(LIS[i], LIS[j]+1)

print(max(LIS))
