import sys

def cantor(n):
    if n == 0:
        token = '-'
        return token

    result = ''
    tmp = cantor(n - 1)
    result += tmp
    for i in range(3 ** (n-1)):
        result += ' '
    result += tmp
    return result

while True:
    try:
        n = int(sys.stdin.readline())
        print(cantor(n))
    except:
        break
        
