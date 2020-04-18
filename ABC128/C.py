N,M = map(int, input().split())
S = [0]*M
for i in range(M):
    S[i] = list(map(int, input().split()))
P = list(map(int, input().split()))


def check(bit):
    f = True
    for i in range(M):
        cnt = 0
        for si in range(len(S[i])):
            if si == 0:
                pass
            else:
                cnt += int(bit[S[i][si]-1])
        if cnt%2 != P[i]:
            f = False
    return f    
    

ans = 0
for i in range(2**N):
    bit = bin(i)[2:].zfill(N)
    if check(bit):
        ans += 1

print(ans)

