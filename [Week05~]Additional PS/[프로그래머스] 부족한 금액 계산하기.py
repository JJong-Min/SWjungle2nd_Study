def solution(price, money, count):
    answer = 0
    total_price = price * ((count*(1 + count))//2)
    result = money - total_price
    if result < 0:
        return -result
    else:
    
        return answer
