import sys

#  내 풀이
T = int(sys.stdin.readline())
for _ in range(T):
    results = sys.stdin.readline().rstrip()
    if 'O' not in results:
        print(0)
    else:
        first_O = results.index('O')
        score = 0

        for idx in range(first_O, len(results)):
            if results[idx] == 'O':
                score += idx + 1 - first_O
            else:
                first_O = idx + 1

        print(score)
        

# 다른 사람 풀이
cnt = int(sys.stdin.readline())
for i in range(cnt):
    score = 0
    combo = 0
    for result in sys.stdin.readline().rstrip():
        if result == "X":
            combo = 0
            continue
        combo += 1
        score += combo
    print(score)
