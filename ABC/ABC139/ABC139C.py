N = int(input())
H = [int(h) for h in input().split()]
A = [0] * N
for n in range(N - 1):
    if H[n] >= H[n+1]:
        if n == 0:
            A[n] = 1
        else:
            A[n] = A[n - 1] + 1

print(max(A))


