'''
import sys

N = sys.stdin.readline().rstrip()

cnt = 1

if int(N) < 10:
    N = '0' + N

first_sum = int(N[0]) + int(N[1])
cycle_result = N[-1] + str(first_sum)[-1]

while int(N) != int(cycle_result):
    if int(cycle_result) < 10:
        cycle_result = '0' + cycle_result

    cycle_sum = int(cycle_result[0]) + int(cycle_result[1])
    cycle_result = str(int(cycle_result[-1] + str(cycle_sum)[-1]))

    cnt += 1

print(cnt)
'''
import sys

N = sys.stdin.readline().rstrip()

if int(N) < 10:
    new_N = N + N
else:
    back_num = int(N[0]) + int(N[1])
    new_N = N[-1] + str(back_num)[-1]


answer = 1

while int(N) != int(new_N):
    if int(new_N) < 10:
        new_N = new_N[-1]+new_N[-1]
    else:
        back_num = int(new_N[0]) + int(new_N[1])
        new_N = new_N[-1] + str(back_num)[-1]



    answer+=1

print(answer)
    
        


