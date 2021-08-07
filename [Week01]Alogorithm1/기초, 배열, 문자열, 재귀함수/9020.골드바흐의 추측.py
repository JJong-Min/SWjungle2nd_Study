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
