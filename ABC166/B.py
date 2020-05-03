N,K=map(int,input().split())
D=[0]*K
A=[0]*K
for i in range(K):
    D[i]=int(input())
    A[i]=list(map(int,input().split()))
d={}
for i in range(1,N+1):
    d[i]=0

for i in range(K):
    for a in A[i]:
        d[a]+=1

ans=0
for i in range(1,N+1):
    if d[i] == 0:
        ans += 1

print(ans)