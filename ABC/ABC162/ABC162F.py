N=int(input())
A=list(map(int,input().split()))

if N%2==0:
    odd=0
    even=0
    for i in range(N):
        if i%2==0:
            odd += A[i]
        else:
            even += A[i]
    print(max(odd,even))

else:
    r1=0
    r2=0
    r3=0
    for i in range(N//2):
        r1+=A[2*i]
        r2+=A[2*i+1]
        r3+=A[2*i+2]
    print(max(r1,r2,r3))
