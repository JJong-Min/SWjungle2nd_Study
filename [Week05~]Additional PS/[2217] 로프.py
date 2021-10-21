import sys
n = int(sys.stdin.readline())
lopes = [int(sys.stdin.readline()) for _ in range(n)]
lopes.sort()
for i in range(n, 0, -1):
    lopes[n - i] *= i

print(max(lopes))
