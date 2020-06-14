N,M,Q=map(int,input().split())
a=[0]*Q
b=[0]*Q
c=[0]*Q
d=[0]*Q
for i in range(Q):
    a[i],b[i],c[i],d[i]=map(int,input().split())

def dfs(part_A,i):
    if i == N:
        A.append(part_A)
    else:
        for a in range(part_A[-1],M+1):
            dfs(part_A+[a],i+1)

A=[]
dfs([1],1)
max_score=0
for An in A:
    score = 0
    for q in range(Q):
        if An[b[q]-1]-An[a[q]-1] == c[q]:
            score += d[q]
    max_score = max(score, max_score)

print(max_score)