from collections import defaultdict

def solution(logs):
    answer = set()
    informations = defaultdict(dict)
    for log in logs:
        test_number, problem_number, score = log.split()
        informations[test_number][problem_number] = int(score)
    
    students_score_per_solved_problem_cnt = defaultdict(dict)
    
    for test_number in informations:
        total_count_of_solve_problem = len(informations[test_number].keys())
        if total_count_of_solve_problem < 5:
            continue
            
        total_score = sum(informations[test_number].values())
        try:
            if students_score_per_solved_problem_cnt[total_count_of_solve_problem][total_score]:
                answer.add(str(students_score_per_solved_problem_cnt[total_count_of_solve_problem][total_score]))
                answer.add(test_number)
        except KeyError:
            students_score_per_solved_problem_cnt[total_count_of_solve_problem][total_score] = test_number
    
    return answer

logs = ["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95", "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100", "1102 9 100"]
print(solution(logs))
