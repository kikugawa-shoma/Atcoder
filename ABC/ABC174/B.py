N,D = map(int,input().split())
X = [0]*N
Y = [0]*N
D = D*D
for i in range(N):
    X[i],Y[i] = map(int,input().split())

ans = 0
for i in range(N):
    d = X[i]**2+Y[i]**2
    if d <= D:
        ans += 1

print(ans)