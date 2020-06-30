D = int(input())
C = [0]*27
C[1:] = list(map(int,input().split()))
S = [[0]*27 for _ in range(D+1)]
for i in range(1,D+1):
    S[i][1:] = list(map(int,input().split()))

T = [0]*(D+1)
T[1:] = [int(input()) for _ in range(D)]
M = int(input())
d = [0]*M
q = [0]*M
for i in range(M):
    d[i],q[i] = map(int,input().split())

last = [[0]*27 for _ in range(D+1)]
score = 0
for i in range(1,D+1):
    score += S[i][T[i]]
    last[i] = last[i-1][:]
    last[i][T[i]] = i
    for j in range(1,27):
        score -= (i-last[i][j])*C[j]
    print(score)

for i in range(M):
    before = T[d[i]]
    after = q[i]
    score -=  S[d[i]][before]
    score += S[d[i]][after]

    cnt = 0
    for j in range(d[i],D+1):
        if last[j][before] != d[i]:
            break
        cnt += 1
    score -= last[d[i]-1]*C[before]*cnt

    cnt = 0
    for j in range(d[i],D+1):
        if last[j][after] != last[d[i]-1]








