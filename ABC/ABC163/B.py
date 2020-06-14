N,M=map(int,input().split())
A=list(map(int, input().split()))

free=N-sum(A)
if free < 0:
    print(-1)
else:
    print(free)