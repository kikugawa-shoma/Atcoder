H, N = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

dp = [[10**10] * (H + 1) for _ in range(N+1)]

for i in range(1, N+1):
    for h in range(1, H+1):
        if h - A[i-1] <= 0:
            dp[i][h] = min(dp[i-1][h], B[i-1])
        else:
            dp[i][h] = min(dp[i-1][h], dp[i][h-A[i-1]] + B[i-1])

print(dp[-1][-1])


