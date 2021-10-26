from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = defaultdict(int)
    member_trees = defaultdict(str)
    seller_infos = defaultdict(int)
    
    for _enroll, _referral in zip(enroll, referral):
        member_trees[_enroll] = (_referral)
        answer[_enroll] = 0


    for _seller, _amount in zip(seller, amount):
        benefit = _amount * 100
        get_benefit_seller = _seller
        while True:
            if get_benefit_seller == '-' or benefit == 0:
                break
            division_benefit = int(benefit * 0.1)
            #print(division_benefit)
            real_benefit = benefit - division_benefit
            answer[get_benefit_seller] += real_benefit
            get_benefit_seller = member_trees[get_benefit_seller]
            benefit = division_benefit
            #print(benefit)
            #print(get_benefit_seller, benefit)

    return list(answer.values())
