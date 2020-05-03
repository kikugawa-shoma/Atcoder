N,M=map(int,input().split())
H=list(map(int,input().split()))
H.insert(0,0)
path=[[] for i in range(N+1)]

for i in range(M):
    A,B=map(int,input().split())
    path[A].append(B)
    path[B].append(A)

ans = 0
for i in range(1,N+1):
    if path[i] == []:
        ans += 1
    else:
        hi=H[i]
        f = True
        for t in path[i]:
            if hi <= H[t]:
                f = False
                break
        if f:
            ans += 1

print(ans)



