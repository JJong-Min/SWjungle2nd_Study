import sys

def set(i, N):
    for j in range(N):
        if(not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + (N - 1)]):
            pos[i] = j
            if i == (N - 1):
                global cnt
                cnt += 1

            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (N - 1)] = True
                set(i + 1, N)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (N - 1)] = False


N = int(sys.stdin.readline())
cnt = 0
pos = [0] * N
flag_a = [False] * N
flag_b = [False] * (N * 2 - 1)
flag_c = [False] * (N * 2 - 1)

set(0, N)
print(cnt)
