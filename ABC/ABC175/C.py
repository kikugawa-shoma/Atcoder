X,K,D = map(int,input().split())
X = abs(X)

if X - K*D <= 0:
    n = X // D
    p = X-n*D
    m = abs(p-D)
    ans = min(m,p)

else:
    ans = X-K*D

print(ans)