from itertools import product
def solution(word):
    alphabets = ['A', 'E', 'I', 'O', 'U']
    per_alpha = []
    for i in range(1, 6):
        per_alpha.extend(product(alphabets, repeat = i))
    per_alpha.sort()
    
    word = tuple(word)

    return per_alpha.index(word) + 1
