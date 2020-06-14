S = input()

N = len(S)
RLLR = []
ans = [0] * N
for i in range(N-1):
    if S[i] == "R" and S[i + 1] == "L":
        RLLR.append(i)
    if S[i] == "L" and S[i+1] == "R":
        RLLR.append(i)
Lchild = 0
Rchild = 0
for i in range(len(RLLR) // 2):
    Lchild = RLLR[2*i+1] - RLLR[2*i]
    ans[RLLR[2*i]] += Lchild // 2
    ans[RLLR[2*i] + 1] += (Lchild - 1) // 2 + 1

    Rchild = RLLR[2*i+2] - RLLR[2*i+1]
    ans[RLLR[2*i+2]] += (Rchild - 1) // 2 +1
    ans[RLLR[2*i+2]+1] += Rchild // 2

Rchild = RLLR[0] + 1
ans[RLLR[0]] += (Rchild - 1) // 2 + 1
ans[RLLR[0]+1] += Rchild // 2

Lchild = (N - 1) - RLLR[-1]
ans[RLLR[-1]] += Lchild // 2
ans[RLLR[-1]+1] += (Lchild - 1) // 2 + 1

print(*ans)


