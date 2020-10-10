H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

mod = 1000000007

L = [[0]*W for _ in range(H)]
R = [[0]*W for _ in range(H)]
U = [[0]*W for _ in range(H)]
D = [[0]*W for _ in range(H)]
M = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(1, W):
        if S[i][j-1] == "." and S[i][j] == ".":
            L[i][j] = L[i][j-1] + 1
for i in range(H):
    for j in range(W-2, -1, -1):
        if S[i][j+1] == "." and S[i][j] == ".":
            R[i][j] = R[i][j+1] + 1
for i in range(1, H):
    for j in range(W):
        if S[i-1][j] == "." and S[i][j] == ".":
            U[i][j] = U[i-1][j] + 1
for i in range(H-2, -1, -1):
    for j in range(W):
        if S[i+1][j] == "." and S[i][j] == ".":
            D[i][j] = D[i+1][j] + 1

blank = 0
for i in range(H):
    for j in range(W):
        M[i][j] = L[i][j] + R[i][j] + U[i][j] + D[i][j] + 1
        if S[i][j] == ".":
            blank += 1


pow2 = [1]*(blank+10)
for i in range(blank+10-1):
    pow2[i+1] = pow2[i]*2
    pow2[i+1] %= mod

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            tmp = pow2[blank-M[i][j]]*(pow2[M[i][j]]-1)
            ans += tmp
            ans %= mod
print(ans)
