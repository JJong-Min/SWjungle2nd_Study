def divided(w):
    _open = 0
    _close = 0
    
    for i in range(len(w)):
        if w[i] == '(':
            _open += 1
        else:
            _close += 1
        if _open == _close:
            return w[:i + 1], w[i + 1:]
        
def isbalanced(w):
    stack = []
    for i in w:
        if i == '(':
            stack.append(i)
        
        else:
            if not stack:
                return False
            stack.pop()
    
    return True
 
def reverse(w):
    u = ''
    for i in w:
        if i == '(':
            u += ')'
        else:
            u += '('
    return u

def solution(p):
    answer = ''
    # 과정 1
    if p == '':
        return answer
    # 과정 2
    u, v = divided(p)
    
    #과정 3
    if isbalanced(u):
        return u + solution(v)
    #과정 4
    else:
        #과정 4 - 1
        answer += '('
        #과정 4 -2
        answer += solution(v)
        # 과정 4 -3
        answer += ')'
        # 과정 4
        u = u[1:-1]
        answer += reverse(u)
        
    return answer
