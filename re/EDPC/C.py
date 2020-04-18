N = int(input())

A = [0] * (N + 1)
B = [0] * (N + 1)
C = [0] * (N + 1)

for i in range(1, N + 1):
    A[i], B[i], C[i] = map(int, input().split())

dp = [[0] * 3 for _ in range(N + 1)]
for i in range(1, N + 1):
    dp[i][0] = A[i] + max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = B[i] + max(dp[i-1][2], dp[i-1][0])
    dp[i][2] = C[i] + max(dp[i-1][0], dp[i-1][1])

print(max(dp[N]))

