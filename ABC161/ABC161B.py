N, M = map(int, input().split())
A = sorted(list(map(int,input().split())),reverse=True)

if A[M-1] < sum(A)/(4*M):
    print("No")
else:
    print("Yes")