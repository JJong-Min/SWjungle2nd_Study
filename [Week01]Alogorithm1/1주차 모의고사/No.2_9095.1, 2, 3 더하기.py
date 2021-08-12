import sys

def recursive_func(n):
    global cnt
    if n < 0:
        return

    elif n == 0:
        cnt += 1
        return

    else:
        for i in range(1, 4):
            recursive_func(n - i)

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    cnt = 0
    recursive_func(n)
    print(cnt)
