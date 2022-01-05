def fib(n):
    _curr, _next = 0, 1
    for _ in range(n):
        _curr, _next = _next, _curr + _next
    return _curr


def fib_recur(n):
    if n == 0:
        return 0
    
    elif n == 1 or n == 2:
        return 1

    return fibo(n - 1) + fibo(n - 2)

def fib(n):
    fiblist = [1, 1]
    if n < 3:
        return 1
    else:
        for i in range(2, n):
            fiblist.append(fiblist[i - 1] + fiblist[i - 2])
    return fiblist[n - 1]


f = [0] * (n + 1)                       # n + 1 만큼 리스트 생성
def pibo(n):
    if(f[n]) != 0:                      # f안에 값이 존재한다면
        return f[n]                     # 재귀함수를 거치지 않고 그대로 출력

    if n < 2: 
        f[n] = n
        return f[n]
    
    else:
        f[n] = pibo(n-1) + pibo(n-2)  # f[n]에 저장
    return f[n]
