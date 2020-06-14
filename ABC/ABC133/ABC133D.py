N = int(input())
A = list(map(int, input().split()))

SUM_A = A[0]
rev = -1
for i in range(N - 2):
    SUM_A += rev*A[i+1]
    rev *= -1

X = [0]*N

X[0] = SUM_A + A[N-1]
for i in range(1, N):
    X[i] = 2 * A[i - 1] - X[i - 1]
print(*X)


