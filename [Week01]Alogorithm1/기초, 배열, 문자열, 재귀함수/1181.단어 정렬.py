import sys

arr = []
N = int(sys.stdin.readline())
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if word not in arr:
        arr.append(word)
    

arr = sorted(arr, key = lambda x: (len(x), x))
for i in arr:
    print(i)
    
