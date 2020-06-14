H, W = map(int, input().split())
S = [input() for _ in range(H)]

L = [[0]*W for _ in range(H)]
R = [[0]*W for _ in range(H)]
U = [[0]*W for _ in range(H)]
D = [[0]*W for _ in range(H)]

for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            L[h][w] = 0
        elif w == 0:
            L[h][w] = 1
        else:
            L[h][w] = L[h][w-1]+1

        if S[h][W-w-1] == "#":
            R[h][W-w-1] = 0
        elif W-w-1 == W-1:
            R[h][W-w-1] = 1
        else:
            R[h][W-w-1] = R[h][W-w]+1

        if S[h][w] == "#":
            U[h][w] = 0
        elif h == 0:
            U[h][w] = 1
        else:
            U[h][w] = U[h-1][w]+1

        if S[H-h-1][w] == "#":
            D[H-h-1][w] = 0
        elif H-h-1 == H-1:
            D[H-h-1][w] = 1
        else:
            D[H-h-1][w] = D[H-h][w]+1

light_num = [[0]*W for _ in range(H)]
for h in range(H):
    for w in range(W):
        light_num[h][w] = L[h][w]+R[h][w]+U[h][w]+D[h][w]

print(max([max(l) for l in light_num])-3)
