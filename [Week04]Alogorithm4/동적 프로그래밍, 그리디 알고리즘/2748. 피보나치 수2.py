import sys

n = int(sys.stdin.readline())

fibonachi = [0 for _ in range(n + 1)]
fibonachi[1] = 1
fibonachi[2] = 1

for i in range(3, n + 1):
    fibonachi[i] = fibonachi[i - 1] + fibonachi[i - 2]

print(fibonachi[n])
