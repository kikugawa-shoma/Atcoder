N=int(input())
A=list(map(int,input().split()))
B=[0]*N
C=[0]*N

for i in range(N):
    B[i]=A[i]+i
    C[i]=i-A[i]

B.sort()
B.insert(0,-2000000000)
B.append(2000000000)
C.sort()
ans=0
for a in C:
    l1=0
    r1=N
    while r1-l1>1:
        m1=(l1+r1)//2
        if B[m1] < a:
            l1=m1
        else:
            r1=m1

    l2=0
    r2=N
    while r2-l2>1:
        m2=(l2+r2)//2
        if B[m2] <= a:
            l2=m2
        else:
            r2=m2

    ans += l2-l1

print(ans)