import sys
# 내 풀이
a = int(sys.stdin.readline())
b = sys.stdin.readline().rstrip()
for idx in range(len(b)-1, -1, -1):
    print(a*(int(b[idx])))

print(a*int(b))

# 다른 사람 풀이
A, B = map(int, input().split())
C = A * B
while B > 0:
    print(A * (B % 10))
    B = B // 10
print(C)
