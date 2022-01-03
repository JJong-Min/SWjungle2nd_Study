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
