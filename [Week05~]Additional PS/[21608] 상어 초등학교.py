

# 실패 코드
import sys
import heapq

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def check_num(n, student, dict_student):
    favorite = []
    no_person = []
    for i in range(n):
        for j in range(n):
            favorite_num = 0
            no_num = 0
            if seats[i][j] == 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if seats[nx][ny] != 0 and seats[nx][ny] in dict_student[student]:
                            favorite_num += 1
                        elif seats[nx][ny] == 0:
                            no_num += 1

            favorite.append((-favorite_num, -no_num, i, j))      
            no_person.append((-no_num, i, j))

    return favorite, no_person
                
def count_point(i, j, seats):
    favorite_num = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n and 0 <= ny < n and seats[nx][ny] in dict_student[seats[i][j]]:
            favorite_num += 1
    if favorite_num > 0:
        return 10 ** (favorite_num - 1)
    else:
        return 0
                              
n = int(sys.stdin.readline())
dict_student = {}
ans = 0
seats = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n**2):
    info = list(map(int, sys.stdin.readline().split()))
    dict_student[info[0]] = info[1:]
seats[1][1] = list(dict_student.keys())[0]

for student in list(dict_student.keys())[1:]:
    favorite_seat, no_person_seat = check_num(n, student, dict_student)
    heapq.heapify(favorite_seat)
    heapq.heapify(no_person_seat)
    
    num1, num2, x, y = heapq.heappop(favorite_seat)
    if num1 != 0:
        seats[x][y] = student
    else:
        num, x, y = heapq.heappop(no_person_seat)
        seats[x][y] = student

favs = []
for i in range(n):
    for j in range(n):
        ans += count_point(i, j, seats)
print(ans)
