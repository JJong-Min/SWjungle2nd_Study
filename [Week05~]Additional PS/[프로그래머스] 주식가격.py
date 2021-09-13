def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for i, price in enumerate(prices):
        if stack:
            while stack[-1][1] > price:
                second, price = stack.pop()
                answer[second] = i - second
        stack.append((i, price))

    while stack:
        i, price = stack.pop()
        answer[i] = len(prices) - i - 1
    return answer
