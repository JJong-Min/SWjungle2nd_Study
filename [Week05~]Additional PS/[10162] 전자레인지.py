import sys

t = int(sys.stdin.readline())
A = B = C = 0
if t % 10:
    print("-1")
else:
    A = t // 300;
    t %= 300;
    B = t // 60;
    t %= 60;
    C = t // 10;
    t %= 10;
    print(A, B, C);
