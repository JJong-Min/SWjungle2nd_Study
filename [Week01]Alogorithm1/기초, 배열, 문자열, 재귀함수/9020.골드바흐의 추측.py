import sys
'''
exist =list(range(10001))

def find_prime(N):
    for i in range(2,N+1):
        if exist[i] ==0:
            continue
        else:
            for k in range(2*i,N+1,i): # 자기 자신을 제외한 그 배수는 모두 지우기
                exist[k] =0

find_prime(10000)
N = int(input())
for _ in range(N):
    
    num = int(input())
    start = num//2
    end = start
    while exist[start]+exist[end]!= num:
        start-=1
        end+=1
        while exist[start]==0 or exist[end]==0:
            start-=1
            end+=1
    print(start, end)
'''
# 풀이 2
def prime_list(n):
    check_prime_num = [True] * n
    for i in range(2, int((n ** 0.5)) + 1):
        if check_prime_num[i] == True:
            for j in range(2 * i, n, i):
                check_prime_num[j] = False
    return [i for i in range(2, n) if check_prime_num[i]]

def get_answer(n):
    prime_arr = prime_list(n)
    idx = max([i for i in range(len(prime_arr)) if prime_arr[i] <= n/2])
    for i in range(idx, -1, -1):
        for j in range(i, len(prime_arr)):
            if prime_arr[i] + prime_arr[j] == n:
                return [prime_arr[i], prime_arr[j]]

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    print(" ".join(map(str, get_answer(N))))

