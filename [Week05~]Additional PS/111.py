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

            favorite.append((-favorite_num, i, j))      
            no_person.append((-no_num, i, j))

    return favorite, no_person
                
                    
                
    
n = int(sys.stdin.readline())
dict_student = {}
seats = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n**2):
    info = list(map(int, sys.stdin.readline().split()))
    dict_student[info[0]] = info[1:]
seats[1][1] = list(dict_student.keys())[0]

for student in list(dict_student.keys())[1:]:
    favorite_seat, no_person_seat = check_num(n, student, dict_student)
    heapq.heapify(favorite_seat)
    heapq.heapify(no_person_seat)
    num, x, y = heapq.heappop(favorite_seat)
    if num != 0:
        seats[x][y] = student
    else:
        
    
    
