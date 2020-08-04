import copy

H,W,K = map(int,input().split())
C = [list(input()) for _ in range(H)]

M = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if C[i][j] == "#":
            M[i][j] = 1

def bit_01(keta):
    ans = []
    for i in range(2**(keta)):
        ans.append("".join(["{:0", str(keta), "b}"]).format(i))
    return ans

vert = bit_01(H)
hori = bit_01(W)

def check(v,h,M):
    M = copy.deepcopy(M)
    for i in range(len(v)):
        if v[i] == "1":
            for ii in range(W):
                M[i][ii] = 0
    for j in range(len(h)):
        if h[j] == "1":
            for jj in range(H):
                M[jj][j] = 0
    S = 0
    for i in range(W):
        for j in range(H):
            S += M[j][i]
    return S == K

ans = 0
for vp in vert:
    for hp in hori:
        if check(vp,hp,M):
            ans += 1

print(ans)
        