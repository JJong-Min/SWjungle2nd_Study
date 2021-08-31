import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    answer = 0
    for i in range(2, n):
        answer = max(answer, abs(arr[i] - arr[i - 2]))
    print(answer)



# 틀린 풀이
import sys

t = int(sys.stdin.readline())

for _  in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    left_standard = arr[0]
    right_standard = arr[1]
    if n % 2 == 0:
        ans = abs(arr[0] - arr[1])
        for i in range(2, n - 1):
            if i % 2 == 0:
                ans = max(ans, abs(left_standard - arr[i]))
                left_standard = arr[i]
            else:
                ans = max(ans, abs(right_standard - arr[i]))
                right_standard = arr[i]
    
    else:
        ans = max(abs(arr[0] - arr[1]), abs(arr[-1] - arr[-2]), abs(arr[-1] - arr[-3]))
        for i in range(2, n - 2):
            if i % 2 == 0:
                ans = max(ans, abs(left_standard - arr[i]))
                left_standard = arr[i]
            else:
                ans = max(ans, abs(right_standard - arr[i]))
                right_standard = arr[i]

    print(ans)
        
                
