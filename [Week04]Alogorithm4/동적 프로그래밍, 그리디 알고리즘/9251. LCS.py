import sys

string1 = ' ' + sys.stdin.readline().rstrip()
string2 = ' ' + sys.stdin.readline().rstrip()
LCS = [[0 for _ in range(len(string2))] for _ in range(len(string1))]

for i in range(1, len(string1)):
    for j in range(1, len(string2)):
        if string1[i] == string2[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i][j - 1], LCS[i - 1][j])

print(LCS[-1][-1])
