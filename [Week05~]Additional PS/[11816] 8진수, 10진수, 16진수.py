import sys

x = sys.stdin.readline().rstrip()

def transform(x):
    if x[:2] == '0x':
        return int(x, 16)
    elif x[0] == '0':
        x = x[0] + 'o' + x[1:]
        return int(x, 8)
    else:
        return int(x)

print(transform(x))
    
