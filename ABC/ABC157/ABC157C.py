N, M = map(int, input().split())
S = [0]*M
C = [0]*M
SC = {}
SC = {1: set([]), 2: set([]), 3: set([])}
for m in range(M):
    S[m], C[m] = map(int, input().split())
    SC[S[m]].add(C[m])

ANS = [0]*N
out = 0
for i in range(1, 4):
    if len(SC[i]) >= 2:
        out = 1
if out == 1:
    print(-1)

else:
    out = 0
    if N == 1:
        if len(SC[1]) == 0:
            ANS[0] = 0
        else:
            ANS[0] = list(SC[1])[0]

    else:
        for i in range(N):
            if i == 0:
                if len(SC[i+1]) == 0:
                    ANS[0] = 1
                elif list(SC[i+1])[0] == 0:
                    out = 1
                else:
                    ANS[0] = list(SC[i+1])[0]
            else:
                if len(SC[i+1]) == 0:
                    ANS[i] = 0
                else:
                    ANS[i] = list(SC[i+1])[0]
    if out == 1:
        print(-1)
    else:
        ans = 0
        for i in range(N):
            ans += ANS[i]*10**(N-i-1)
        print(ans)





