import sys
n = int(sys.stdin.readline())
tiles = [0 for _ in range(n + 1)]
tiles[0] = 1
tiles[1] = 2
for i in range(2, n):
    tiles[i] = (tiles[i - 1] + tiles[i - 2]) % 15746
    
print(tiles[n - 1])
