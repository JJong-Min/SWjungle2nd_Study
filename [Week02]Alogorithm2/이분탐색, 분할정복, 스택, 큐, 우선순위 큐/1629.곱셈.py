import sys

def search_mod(a, b, c):
    if b == 1:
        return a % c

    temp = search_mod(a, b // 2, c)

    if b % 2 == 0:
        return temp * temp % c

    else:
        return temp * temp *A % c

A, B, C = map(int, sys.stdin.readline().split())

print(search_mod(A, B, C))
