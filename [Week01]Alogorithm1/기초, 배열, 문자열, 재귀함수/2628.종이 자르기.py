import sys

width, height = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())
height_arr = [0 for _ in range(height)]
width_arr = [0 for _ in range(width)]

for _ in range(T):
    cutting_num1, cutting_num2 = map(int, sys.stdin.readline().split())
    if cutting_num1 == 0:
        height_arr[cutting_num2 - 1] = 1
    else:
        width_arr[cutting_num2 - 1] = 1


width_length = []
height_length = []
width_cnt = 0
height_cnt = 0

for width_num in width_arr:
    width_cnt += 1
    if width_num == 0:
        continue
    else:
        width_length.append(width_cnt)
        width_cnt = 0

width_length.append(width_cnt)

for height_num in height_arr:
    height_cnt += 1
    if height_num == 0:
        continue
    else:
        height_length.append(height_cnt)
        height_cnt = 0

height_length.append(height_cnt)
            
print(max(height_length)*max(width_length))