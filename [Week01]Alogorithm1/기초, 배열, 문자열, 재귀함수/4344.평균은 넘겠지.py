import sys

C = int(sys.stdin.readline())

for _ in range(C):
    informations = list(map(int, sys.stdin.readline().split()))
    student_num = informations[0]
    student_scores = informations[1:]
    avg_score = sum(student_scores) / student_num
    cnt = 0

    for student_score in student_scores:
        if student_score > avg_score:
            cnt += 1

    over_avg_students_ratio = cnt/student_num * 100
    print(format(over_avg_students_ratio, ".3f"), "%", sep='')
    
