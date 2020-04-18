N, W = map(int, input().split())

w = [0] * (N + 1)
v = [0] * (N + 1)
for i in range(1, N + 1):
    w[i], v[i] = map(int, input().split())

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for weight in range(1, W + 1):
        if weight - w[i] >= 0:
            dp[i][weight] = max(dp[i][weight], dp[i - 1][weight-w[i]] + v[i])
        dp[i][weight] = max(dp[i-1][weight], dp[i][weight])

print(dp[N][W])