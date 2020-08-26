N = int(input())
A = list(map(int,input().split()))

dai = 0

for i in range(1,N):
    if A[i-1] > A[i]:
        d = A[i-1] - A[i]
        A[i] += d
        dai += d

print(dai)