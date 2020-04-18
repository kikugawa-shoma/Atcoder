import bisect

N, W = map(int, input().split())
w = [0] * (N + 1)
v = [0] * (N + 1)

for i in range(1, N + 1):
    w[i], v[i] = map(int, input().split())
INF = 1000000010
MAX_V = 100010
dp = [[INF] * MAX_V for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for value in range(MAX_V):
        if value <= v[i]:
            dp[i][value] = min(dp[i-1][value], w[i])
        else:
            dp[i][value] = min(dp[i - 1][value], dp[i-1][value-v[i]] + w[i])

print(bisect.bisect_right(dp[N], W)-1)
