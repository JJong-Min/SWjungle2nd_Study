import sys

N = int(sys.stdin.readline())

if N <=99:
    print(N)
else:
    cnt = 99
    for num in range(100, N + 1):
        num = str(num)
        before_number = num[1]
        gap = int(num[0]) - int(num[1])
        check = True
        for idx in range(2, len(num)):
            if gap == (int(before_number) - int(num[idx])):
                before_number = num[idx]
            else:
                check = False
                break

        if check:
            cnt += 1

    print(cnt)


        
    
