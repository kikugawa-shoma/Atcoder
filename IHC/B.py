D = int(input())
C = [0]*27
C[1:] = list(map(int,input().split()))
S = [[0]*27 for _ in range(D+1)]
for i in range(1,D+1):
    S[i][1:] = list(map(int,input().split()))

T = [0]*(D+1)
T[1:] = [int(input()) for _ in range(D)]

last = [0]*27
score = 0
for i in range(1,D+1):
    score += S[i][T[i]]
    last[T[i]] = i
    for j in range(1,27):
        score -= (i-last[j])*C[j]
    print(score)
