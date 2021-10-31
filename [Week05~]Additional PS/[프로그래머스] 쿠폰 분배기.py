from collections import defaultdict
def solution(id_list, k):
    answer = 0
    total_count_of_perchase_per_customers = defaultdict(int)
    for ids in id_list:
        ids = ids.split(' ')
        check_get_coupon = defaultdict(int)
        for customer in ids:
            if total_count_of_perchase_per_customers[customer] < k and check_get_coupon[customer] == 0: 
                total_count_of_perchase_per_customers[customer] += 1
                check_get_coupon[customer] = 1
    answer = sum(list(total_count_of_perchase_per_customers.values()))
    return answer
