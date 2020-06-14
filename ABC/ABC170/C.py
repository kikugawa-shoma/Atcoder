
X,N = map(int,input().split())
P = set(map(int,input().split()))

for i in range(200):
    y,yy = X-i,X+i
    if y not in P:
        print(y)
        break
    elif yy not in  P:
        print(yy)
        break
