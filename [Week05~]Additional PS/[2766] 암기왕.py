import sys
t = int(sys.stdin.readline())

for _ in range(t):
    note1 = int(sys.stdin.readline())
    note_1 = list(map(int, sys.stdin.readline().split()))
    note2 = int(sys.stdin.readline())
    note_2 = list(map(int, sys.stdin.readline().split()))
    note_1.sort()
    
    for i in note_2:
        flag = False
        left = 0
        right = note1 - 1
        while left <= right:
            mid = (left + right) // 2
            if note_1[mid] == i:
               print(1)
               flag = True
               break
            elif note_1[mid] < i:
                left = mid + 1
            else:
                right = mid - 1

        if not flag:
            print(0)
