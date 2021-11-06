from itertools import combinations
import sys

input= sys.stdin.readline

N, K = map(int, input().split())

alphabet = {'a':True, 'b':False, 'c':True, 'd':False,'e':False,'f':False,'g':False,'h':False,'i':True,'j':False,'k':False,'l':False,'m':False,'n':True,'o':False,'p':False,  'q':False,'r':False,'s':False,'t':True,'u':False,'v':False,'w':False,'x':False,'y':False,'z':False}

# a c n t i  5개는 무조건 가르쳐야함 
# alpha = ['b','d','e','f','g','h','j','k','l','m','o','p', 'q','r','s','u','v','w','x','y','z']


words = []
chars = []


def solution():
    MAXi = 0
 
    for i in range(N):
        word = input()[3:-4]
        words.append(list(word))
        for char in word:
            if not alphabet[char]:
                chars.append(char)
                alphabet[char]=True

    if K<=4:
        return 0

    num = len(chars)
    if K-5>=num:
        return N
    else:
        arr = list(combinations(chars,K-5))

        for i in range(len(arr)):
            for char in chars:
                alphabet[char]=False #초기화
            
            for j in arr[i]:
                alphabet[j]=True
            
            answer = N
            for word in words:
                for l in word:
                    if alphabet[l]==False:
                        answer-=1
                        break
            MAXi=max(MAXi,answer)
        return MAXi


print(solution())
